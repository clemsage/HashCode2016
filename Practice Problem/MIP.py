import pulp
import math
import time


def mip(painting, n, m):
    """
    :param painting: Dictionary representing the n*m painting
    :param m: Width of the painting
    :param n: Length of the painting
    :return: List of the optimal commands
    """
    start_mip = time.time()

    print 'Define the problem'
    problem = pulp.LpProblem('PaintingOperations', sense=pulp.LpMinimize)

    # Preprocessing : determine the maximum length of vertical and horizontal lines
        #... To be done
    max_vertical = n + 1
    max_horizontal = m + 1

    print "Define all the valid commands for squares..."
    Sq = [(R, C, S) for R in range(n) for C in range(m) for S in range(1 + abs((min(m, n)-1)/2)) if R+S < n and R-S >= 0 and C+S < m and C-S >= 0]
    print "Done. Total number of squares found: %d" % len(Sq)

    print "Removing useless squares..."
    # Remove squares which have more empty cells than filled cells
    for sq in Sq:
        if sum(painting[sq[0]-sq[2]+r,sq[1]-sq[2]+c] for r in range(2*sq[2]+1) for c in range(2*sq[2]+1)) <= 0.5 * len([1 for r in range(2*sq[2]+1) for c in range(2*sq[2]+1)]):
            Sq.remove(sq)
    print "Done. New total number of squares: %d. Time taken : %d sec" % (len(Sq), (time.time() - start_mip))
    
    print 'Define all the valid and useful horizontal lines...'
    Li = []
    for R1 in range(n):
        for C1 in range(m):
            if painting[R1, C1] == 1:
                for c in range(m-C1):
                    if painting[R1, C1+c] == 0:
                        Li.append((R1, C1, R1, C1+c-1))
                        break
    print "Done. Total number of horizontal lines found: %d" % len(Li)

    print 'Define all the valid and useful vertical lines...'
    Li2 = []
    for C1 in range(m):
        for R1 in range(n):
            if painting[R1, C1] == 1:
                for r in range(n-R1):
                    if painting[R1+r, C1] == 0:
                        Li.append((R1, C1, R1+r-1, C1))
                        break
    print "Done. Total number of lines found: %d. Time taken : %d sec" % (len(Li), (time.time() - start_mip))

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
