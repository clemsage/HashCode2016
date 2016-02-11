from tools import *
import operator

def rank_orders(orders,drone,weights,warehouses,products):
    C = {}
    for order in orders:
        C[order.ID] = distance(drone,order) + sum(order.items[item]*weights[item] for item in order.items.keys())

    sorted_C = sorted(C.items(), key=operator.itemgetter(1))

    #Attribute an order corresponding to the first
    commands = {}
    for c in sorted_C:
        for itemID, itemval in orders[c[0]].items.items():
            if warehouses[[warehouse for warehouse in warehouses if warehouse.coords == drone.position][0]].stock[itemID] > 0:
                commands[c[0],itemID] = max(num for num in range(1+min(warehouses[[warehouse for warehouse in warehouses if warehouse.coords == drone.position][0]].stock[itemID], itemval)) if drone.charge + num * products[itemID].weigth <= overload )
                OK






def ranks = rank_warehouse(warehouse,drone)

    ranks()
    return