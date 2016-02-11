class drone:
    def __init__(self, i, x, y, P):
        self.ID = i
        self.position = [x, y]
        self.charge = 0
        self.time = 0
        self.mouvement = 0
        self.loaded = 0
        self.load = {p : 0 for p in range(len(P))}
        self.weights = P
        
class product:
    def __init__(self, i, w):
        self.ID = i
        self.weight = w

class order:
    def __init__(self, i, x, y, l, items):
        self.ID = i
        self.coords = [x, y]
        self.L = l
        self.items = items
        self.completed = 0
        
class warehouse:
    def __init__(self, i, x, y, stock):
        self.ID = i
        self.coords = [x, y]
        self.stock = stock

