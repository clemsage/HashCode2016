from math import sqrt, ceil

def distance(drone, centre):
    return sqrt((drone.position[1]-centre.coords[1])**2
                + (drone.position[0]-centre.coords[0])**2)

def load(drone_id, tag, warehouse_id, product_id, n_items):
    wh = warehouses[warehouse_id]
    dr = drones[drone_id]
    dr.mouvement = 1
    dr.time = dr.time + ceil(distance(dr, wh))+1
    if tag == 'L':
        wh.stock[product_id] = wh.stock[product_id] - n_items
        dr.load[product_id] = dr.load[product_id] + n_items
        dr.loaded = 1
    elif tag == 'U':
        wh.stock[product_id] = wh.stock[product_id] + n_items
        dr.load[product_id] = dr.load[product_id] - n_items
        dr.loaded = 0
    dr.charge = sum([n*self.weights[product_type] for product_type, n in self.load.items()])
    dr.position = wh.coords
    dr.mouvement = 0


def deliver(drone_id, tag, order_id, product_id, n_items):
    order = orders[order_id]
    dr = drones[drone_id]
    dr.mouvement = 1
    if tag == 'D':
        order.items[product_id] = order.items[product_id] - n_items
        dr.load[product_id] = dr.load[product_id] - n_items
        dr.loaded = 0
    dr.charge = sum([n*self.weights[product_type] for product_type, n in self.load.items()])
    if dr.charge == 0:
        dr.loaded = 0
    else:
        dr.loaded = 1
    dr.mouvement = 0

    # on regarde si l'order est completed
    if len(list(set(order.values())))==1:
        order.completed = 1




