def generator(n:int = 1):
    tmp = n
    while tmp >= 0:
        yield tmp
        tmp -= 1

for i in generator(10):
    print(i)