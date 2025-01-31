import math


class Point():
    def __init__(self, X: float = 0, Y:float = 0):
        self.x = X
        self.y = Y
    
    def show(self):
        print(f"X: {self.x} \t Y: {self.y}")

    def move(self, X:float = 0, Y:float = 0):
        self.x = X
        self.y = Y
    
    def dist(self, other):
        if isinstance(other, Point):
            return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.x - other.y, 2))
        else:
            return NotImplemented