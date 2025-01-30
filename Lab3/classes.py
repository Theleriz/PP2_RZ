import math


class Console:
    """first class of task"""
    string = ''

    def getString(self):
        self.string = input();


    def printString(self):
        print(self.string)


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


class Account:
    balance = 0

    def __init__(self, owner:str = 'null'):
        self.owner = owner

    def deposit(self, value:int = 0):
        self.balance += value

    def withdraw(self, value:int = 0):
        if self.balance >= value:
            self.balance -= value
        else:
            print('Not enough balance to withdraw.')

pepe = Account('Pepe')
pepe.deposit(1000)
pepe.withdraw(500)
print(pepe.balance)

class PrimeList:
    def __primary(self, x):
        div = []
        for i in range(1, int(math.sqrt(x)) + 1):
            if(x % i == 0 and x > 1):
                div.append(i)
        return len(div) == 1
    
    def __init__(self, lst: list = []):
        self.lst = list(filter(self.__primary, lst))
        print(self.lst)


p1 = PrimeList([1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 11])
