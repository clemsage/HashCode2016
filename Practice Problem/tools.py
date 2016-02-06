def paint(toile, command):
    com = command.split(' ')
    if com[0] == 'PAINT_SQUARE':
        paint_square(toile, com[1], com[2], com[3])
    elif com[0] == 'PAINT_LINE':
        paint_line(toile, com[1], com[2], com[3], com[4])
    elif com[0] == 'ERASE_CELL':
        erase_cell(toile, com[1], com[2])
    else:
        print 'Erreur, commande inconnue !'

def paint_square(toile, R, C, S):
    N, M = len(toile), len(toile[0])
    if S>0:
        for r in range(2*S+1):
            for c in range(2*S+1):
                toile[R-S+r][C-S+c] = '#'
    else:
        print 'Rentrer un rayon positif !'

def paint_line(toile, R1, C1, R2, C2):
    if R1 == R2:
        for r in range(abs(C2-C1)):
            toile[R1][min(C1, C2) + r] = '#'
    elif C1 == C2:
        for c in range(abs(R2-R1)):
            toile[min(R1, R2) + c][C1] = '#'
    else:
        print "Commande non valide. Ce n'est pas une ligne"

def erase_cell(toile, R, C):
    toile[R][C] = '.'
    
    
