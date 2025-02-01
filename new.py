import math


class Console:
    def __init__(self):
        self.string = ''

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string)


class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


class Rectangle(Shape):
    def __init__(self, length: float = 0, width: float = 0):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"X: {self.x} \t Y: {self.y}")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        if isinstance(other, Point):
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        raise NotImplemented


class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, value: int = 0):
        self.balance += value

    def withdraw(self, value: int = 0):
        if self.balance >= value:
            self.balance -= value
        else:
            print('Check the balance.')


class PrimeList:
    def _is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def __init__(self, lst=None):
        if lst is None:
            lst = []
        self.lst = [num for num in lst if self._is_prime(num)]
        print(self.lst)



pepe = Account('Pepe')
pepe.deposit(1000)
pepe.withdraw(500)
print(pepe.balance)

p1 = PrimeList([1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 11])
