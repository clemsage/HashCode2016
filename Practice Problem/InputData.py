def input_data(path, ext):
    with open(path+ext, 'r') as fichier:
        contenu = map(lambda x: x.replace('\n', '').split(' '), fichier.readlines())
        N, M = map(int, contenu[0])
        painting = [[contenu[1+n][0][m] for m in range(M)] for n in range(N)]
        return N, M, painting


def binary_transformation(painting, n, m):
    '''
    :param painting: Lists of '#' and '.'
    :return: Dictionary of '1' and '0'
    '''
    output_painting = {}

    for i in range(n):
        for j in range(m):
            if painting[i][j] == '#':
                output_painting[i,j] = 1
            elif painting[i][j] == '.':
                output_painting[i,j] = 0

    return output_painting


