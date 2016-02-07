import pulp
import math


def mip(painting, m, n):
    """
    :param painting: Dictionary representing the m*n painting
    :param m: Width of the painting
    :param n: Length of the painting
    :return: List of the optimal commands
    """

    # Define the problem
    problem = pulp.LpProblem('PaintingOperations', sense=pulp.LpMinimize)

    # Define all the valid commands for painting squares and lines
    Sq = [(R, C, S) for R in range(n) for C in range(m) for S in range(math.floor((min(m, n)-1)/2)) if R+S < n and R-S >= 0 and C+S < m and C-S >= 0]
    Li = [(R1, C1, R2, C2) for R1 in range(n) for C1 in range(m) for R2 in range(n) for C2 in range(m) if R1 == R2 or C1 == C2]

    # Define the variables
    squares = {}
    for sq in Sq:
        squares[sq] = pulp.LpVariable('square_%d_%d_%d' % sq, lowBound=0, upBound=1, cat=pulp.LpInteger)

    lines = {}
    for li in Li:
        lines[li] = pulp.LpVariable('line_%d_%d_%d_%d' % li, lowBound=0, upBound=1, cat=pulp.LpInteger)

    erases = {}
    for i in range(n):
        for j in range(m):
            erases[i, j] = pulp.LpVariable('erase_%d_%d' % (i, j), lowBound=0, upBound=1, cat=pulp.LpInteger)

    painted = {}
    for i in range(n):
        for j in range(m):
            painted[i, j] = pulp.LpVariable('painted_%d_%d' % (i,j), lowBound=0, upBound=1, cat=pulp.LpInteger)

    # Define the objective : total number of painting commands
    obj = pulp.LpAffineExpression()
    obj += sum(squares[sq] for sq in Sq) + sum(lines[li] for li in Li) + sum(erases[i, j] for i in range(n) for j in range(m))
    problem += obj

    # Define the constraints
    for i in range(n):
        for j in range(m):
            problem += pulp.LpConstraint(painted[i, j] - painting[i, j], pulp.LpConstraintEQ, 'InputPainting', 0)
            problem += pulp.LpConstraint(painted[i, j] - sum(squares[sq] for sq in Sq if math.fabs(i-sq[0]) <= sq[2] and math.fabs(j-sq[1]) <= sq[2]) - sum(lines[li] for li in Li if min(li[0], li[2]) <= i <= max(li[0], li[2]) and min(li[1], li[3]) <= j <= max(li[1], li[3])) - erases[i,j], pulp.LpConstraintEQ, 'OperationsPerformed', 0)

    # Solve the problem
    status = problem.solve()

    # Edit the list of the optimal commands
    commands = []
    for sq in Sq:
        if squares[sq].value == 1:
            commands.append('PAINT_SQUARE %d %d %d' % sq)

    for li in Li:
        if lines[li].value == 1:
            commands.append('PAINT_LINE %d %d %d %d' % li)

    for i in range(n):
        for j in range(m):
            commands.append('ERASE_CELL %d %d' % (i,j))

    return commands
