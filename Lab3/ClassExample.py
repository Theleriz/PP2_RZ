import math


class MyPointClass:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
    

    def __repr__(self):
        return f"x: {self.x} y: {self.y}"
    

    def __add__(self, other):
        if isinstance(other, MyPointClass):
            return MyPointClass(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
    
    
    def __sub__(self, other):
        if isinstance(other, MyPointClass):
            return MyPointClass(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, MyPointClass):
            if((self.x == other.y) and (self.y == other.y)):
                return True
            else:
                return False
        else:
            return NotImplemented

    def lenght(self) -> float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)) 



fr = MyPointClass(1, 1)
sc = MyPointClass(2, 3)

print(fr == sc)

