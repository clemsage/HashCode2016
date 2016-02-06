path = 'Practice Problem/Downloads'
files = ['/right_angle.in', '/logo.in', '/learn_and_teach.in']


with open(path+files[0], 'r') as fichier:
    contenu = map(lambda x: x.replace('\n', '').split(' '), fichier.readlines())
    print contenu[0]
    print contenu[1]
    
