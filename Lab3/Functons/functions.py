from math import sqrt
from math import pow
from itertools import permutations


def gramsToOunces(grams: float) -> float:
    ounces = 28.3495231 * grams
    return ounces


def fahrenheitToCentigrate(F: float) -> float:
    C = (5 / 9) * (F - 32)
    return C    


def solve(numheads: int, numlegs: int):
    rabits = numlegs / 2 - numheads
    chickens = 2 * numheads - numlegs / 2
    print(f"Number of rabits {rabits}, and number of chickens {chickens}")


def isPrime(x: int) -> bool:
        div = []
        for i in range(1, int(sqrt(x)) + 1):
            if(x % i == 0 and x > 1):
                div.append(i)
        return len(div) == 1


def primeList(lst:list) -> list:
    """this function for task 4"""
    answerList = []
    lstBool = []
    j = 0
    for i in lst:
        lstBool.append(isPrime(i))
    
    for i in lstBool:
        if lstBool[j] == True:
            answerList.append(lst[j])
        j += 1
    return answerList


def perm() :
    string = input()
    stringPerm = list(permutations(string))
    print(stringPerm)
    for i in stringPerm:
        print(str(i))


def reverseString():
    words = list(input().split())
    words = reversed(words)
    string = ""
    for i in words:
        string = string + i + " "
    print(string)


def isThree(lst: list) -> bool:
    for i in range(len(lst) - 1):  
         if lst[i] == 3 and lst[i + 1] == 3:  
            return True
    return False


def volumeOfSphere(R: float) -> float:
    pi = 3.14
    return (4 / 3) * pi * R * R * R


def uniq(lst:list) -> list:
    answerList = []
    for i in lst:
        if not (i in answerList):
            answerList.append(i)
    return answerList


