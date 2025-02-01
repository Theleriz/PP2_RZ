import math

def gramsToOunces(grams):
    ounces = 28.3495231 * grams
    return ounces


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"x: {self.x} y: {self.y}"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
        
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            if((self.x == other.y) and (self.y == other.y)):
                return True
            else:
                return False
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
                return (self.x * other.x) + (self.y * other.y)
        else:
            return NotImplemented

    def lenght(self) -> float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)) 

    def unitForm(self):
        return Vector((self.x / self.lenght()), (self.y / self.lenght()))
    
    def sign(self, other):
        if isinstance(other, Vector):
            return (self.x * other.y) - (self.y * other.x)
        else:
            return NotImplemented
        
    def angle(self, other):
        if isinstance(other, Vector):
            cosAngle = (self * other) / (math.sqrt(self.lenght() * other.lenght()))
            return self.sign(self, other) * math.acos(cosAngle)
        else:
            return NotImplemented

EX = Vector(1, 0)
EY = Vector(0, 1)    



    





