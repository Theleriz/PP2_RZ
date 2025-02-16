def sequence(n: int):
    it = 0
    while it <= n:
        if it % 3 == 0 and it % 4 == 0:
            yield it
        it += 1

for i in sequence(int(input())):
    print(i)