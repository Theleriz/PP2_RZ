def isPolindrom(x):
    reversX = reversed(x)
    for i in range(len(x)):
        index = len(x) - i - 1
        if(x[i] != x[index]):
            return False
    else:
        return True
    
