import math
def primary(x):
        div = []
        for i in range(1, int(math.sqrt(x)) + 1):
            if(x % i == 0 and x > 1):
                div.append(i)
        return len(div) == 1

def generateOfPrimeNumber(lenght:int = 0):
    for i in range(2, lenght):
        if primary(i) == True:
            yield i
        

for i in generateOfPrimeNumber(1000):
    print(i, end=" ")

    
    

