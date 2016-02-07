import pulp
import math


def mip(painting, n, m):
    """
    :param painting: Dictionary representing the n*m painting
    :param m: Width of the painting
    :param n: Length of the painting
    :return: List of the optimal commands
    """

    print 'Define the problem'
    problem = pulp.LpProblem('PaintingOperations', sense=pulp.LpMinimize)

    # Preprocessing : determine the maximum length of vertical and horizontal lines
        #... To be done
    max_vertical = 10
    max_horizontal = 13

    print 'Define all the valid commands for painting squares and lines'
    Sq = [(R, C, S) for R in range(n) for C in range(m) for S in range(1 + int(math.floor((min(m, n)-1)/2))) if R+S < n and R-S >= 0 and C+S < m and C-S >= 0]
    Li = [(R1, C1, R2, C2) for R1 in range(n) for C1 in range(m) for R2 in range(n) for C2 in range(m) if (R1 == R2 and math.fabs(C1-C2) < max_horizontal) or (C1 == C2 and math.fabs(R1-R2) < max_vertical)]

    print 'Number of squares founded : %d' % len(Sq)
    print 'Number of lines founded : %d' % len(Li)

    # Remove the lines with the same beginning and ending cells and those which length is equal to one cell (already dealt by "square" variables)
    for li in Li:
        Li.remove((li[2], li[3], li[0], li[1]))

    print 'Number of lines founded : %d' % len(Li)

    # Remove the lines for which its beginning or ending cell corresponds to a cell which has to remain clear
    for li in Li:
        if painting[li[0], li[1]] == 0 or painting[li[2], li[3]] == 0:
            Li.remove(li)

    print 'Number of lines founded : %d' % len(Li)

    # Remove squares and lines which have more than 50% of empty cells inside them
        #To do...

    print 'Define the variables'
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

    print 'Define the objective : total number of painting commands'
    obj = pulp.LpAffineExpression()
    obj += sum(squares[sq] for sq in Sq) + sum(lines[li] for li in Li) + sum(erases[i, j] for i in range(n) for j in range(m))
    problem += obj

    print 'Define the constraints'
    for i in range(n):
        for j in range(m):
            problem += pulp.LpConstraint(painted[i, j] - painting[i, j], pulp.LpConstraintEQ, 'InputPainting_%d_%d' % (i, j))
            problem += pulp.LpConstraint(painted[i, j] - sum(squares[sq] for sq in Sq if math.fabs(i-sq[0]) <= sq[2] and math.fabs(j-sq[1]) <= sq[2]) - sum(lines[li] for li in Li if min(li[0], li[2]) <= i <= max(li[0], li[2]) and min(li[1], li[3]) <= j <= max(li[1], li[3])) + erases[i, j], pulp.LpConstraintEQ, 'OperationsPerformed_%d_%d' % (i, j))

    print 'Solve the problem'
    status = problem.solve()

    # Check that the resulting picture is identical to the target one
    for i in range(n):
        for j in range(m):
            if painting[i, j] != painted[i, j].value():
                raise 'Painting value for (%d, %d) : %d and MIP value : %d' % (i, j, painting[i,j], painted[i, j].value())

    print 'Edit the list of the optimal commands'
    commands = []
    for sq in Sq:
        if squares[sq].value() == 1:
            commands.append('PAINT_SQUARE %d %d %d' % sq)

    for li in Li:
        if lines[li].value() == 1:
            commands.append('PAINT_LINE %d %d %d %d' % li)

    for i in range(n):
        for j in range(m):
            if erases[i, j].value() == 1:
                commands.append('ERASE_CELL %d %d' % (i,j))

    return commands