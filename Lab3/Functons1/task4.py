from math import sqrt


def isPrime(x: int) -> bool:
        div = []
        for i in range(1, int(sqrt(x)) + 1):
            if(x % i == 0 and x > 1):
                div.append(i)
        return len(div) == 1


def filter_prime(lst:list) -> list:
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