class drone:
    def __init__(self, i, x, y):
        self.ID = i
        self.position = [x, y]
        self.charge = 0
        self.time = 0

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
        
class warehouse:
    def __init__(self, i, x, y, stock):
        self.ID = i
        self.coords = [x, y]
        self.stock = stock

