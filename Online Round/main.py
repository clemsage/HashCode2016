from tools import *
from objets import *
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
    products = []
    weights = map(int, list(contenu[2].split(' ')))
    for i in range(P):
        products.append(product(i, weights[i]))
        
    W = int(contenu[3])
    warehouses = []
    for l in range(W):
        a, b = map(int, contenu[4+2*l].split(' '))
        store = map(int, contenu[5+2*l].split(' '))
        stock = {}
        for product_id in list(set(store)):
            stock[product_id] = store.count(product_id)
        warehouses.append(warehouse(l, a, b, stock))

    drones = []
    for i in range(D):
        drones.append(drone(i, warehouses[0].coords[0], warehouses[0].coords[1]))

    C = int(contenu[4+2*W])
    orders = []
    for l in range(C):
        a, b = map(int, contenu[5+2*W+3*l].split(' '))
        L = int(contenu[6+2*W+3*l])
        items = map(int, contenu[7+2*W+3*l].split(' '))
        item = {}
        for product_id in list(set(items)):
            item[product_id] = items.count(product_id)
        orders.append(order(l, a, b, L, item))


print 'Total time : %f min' % ((time.time() - start)/60.)
