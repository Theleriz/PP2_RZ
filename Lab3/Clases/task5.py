import math


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