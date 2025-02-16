def generator(n:int = 1):
    it = 0
    while it <= n:
        yield it ** 2
        it += 1

for i in generator(10):
    print(i, end=" ")