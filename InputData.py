path = 'Practice Problem/Downloads'
files = ['/right_angle.in', '/logo.in', '/learn_and_teach.in']


with open(path+files[0], 'r') as fichier:
    contenu = map(lambda x: x.replace('\n', '').split(' '), fichier.readlines())
    N, M = map(int, contenu[0])
    
    print N, M
    print contenu[0]
    print contenu[1]
    print contenu[1][0][0]
    
    painting = [[contenu[1+n][0][m] for m in range(M)] for n in range(N)]
    print painting[0]
    
