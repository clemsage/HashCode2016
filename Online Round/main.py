from tools import *
import MIP
import time

# Measure the time spent to solve the MIP
start = time.time()

# Read the data
path = 'Downloads/'
files = ['busy_day.in', 'mother_of_all_warehouses.in', 'redundancy.in']
path += files[0]

with open(path, 'r') as fichier:
    contenu = fichier.readlines()
    row, col, D, T, max_load = map(int, contenu[0].split(' '))
    P = int(contenu[1])
    weights = map(int, list(contenu[2].split(' ')))
    W = int(contenu[3])
    warehouses = {}
    id_warehouses = {}
    for l in range(W):
        a, b = map(int, contenu[4+2*l].split(' '))
        store = map(int, contenu[5+2*l].split(' '))
        warehouses[a, b] = store
        id_warehouses[l] = [a, b]

    C = int(contenu[4+2*W])
    
    orders = {}
    for l in range(C):
        a, b = map(int, contenu[5+2*W+3*l].split(' '))
        L = int(contenu[6+2*W+3*l]) # useless
        items = map(int, contenu[7+2*W+3*l].split(' '))
        orders[a, b] = items


print 'Total time : %f min' % ((time.time() - start)/60.)
