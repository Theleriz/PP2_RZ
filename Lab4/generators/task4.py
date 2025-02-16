def squares(a:int = 0, b:int = 0):
    holder = a
    while holder <= b:
        yield holder ** 2
        holder += 1

for i in squares(-1, 10):
    print(i)