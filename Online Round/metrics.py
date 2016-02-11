from tools import *
import operator

def rank_orders(orders,drone,weights, warehouses):
    C = {}
    for order in orders:
        C[order.ID] = distance(drone,order) + sum(order.items[item]*weights[item] for item in order.items.keys())

    sorted_C = sorted(C.items(), key=operator.itemgetter(1))

    #Attribute an order corresponding to the first
    for c in sorted_C:
        for itemID, itemval in orders[c[0]].items.items():
            if itemval <= warehouses[[warehouse for warehouse in warehouses if warehouse.coords == drone.position][0]].stock[itemID]
                drones






def ranks = rank_warehouse(warehouse,drone)

    ranks()
    return