def generatorOfEvenNumber(n: int = 0):
    it = 0
    while it <= n:
        if it % 2 == 0:
            yield it
        it += 1

for i in generatorOfEvenNumber(int(input())):
    print(i, end=" ")