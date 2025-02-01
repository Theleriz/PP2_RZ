class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

class Square(Shape):
    def __init__(self, lenght: float = 0) -> float:
        self.lenght = lenght

    def area(self):
        print(self.lenght * self.lenght)
    

class Rectangle(Shape):
    
    def __init__(self, lenght:float = 0, width: float = 0):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width