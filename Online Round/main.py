from tools import *
from objets import *
import MIP
from metrics import *
import time

# Measure the time spent to solve the MIP
start = time.time()

# Read the data
path = 'Downloads/'
files = ['busy_day.in', 'mother_of_all_warehouses.in', 'redundancy.in']
path += files[0]

# Initialize objects
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
        drones.append(drone(i, warehouses[0].coords[0], warehouses[0].coords[1],P))

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

# Simulation loop over time
for t in range(T):
    # Select the free drones
    drones_to_load = [drone for drone in drones if drone.mouvement == 0 and drone.loaded == 0]
    drones_to_deliver = [drone for drone in drones if drone.mouvement == 0 and drone.loaded == 1]

    # Compute the metrics for the drones free
    drones_order = list()
    for drone in drones_to_deliver:
        drones_order.append(rank_orders(orders,drone,weights,warehouses))

    for drone in drones_to_load:
        drones_order.append(rank_warehouse(warehouses, drone))

    # Update the coordinates and states (mouvement & loaded)  of the drones

    # Update the stocks of the warehouses

    # Update the orders (completed or not, objects which hasn't been...)



print 'Total time : %f min' % ((time.time() - start)/60.)
