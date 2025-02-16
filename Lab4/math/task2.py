def trapezoidArea(height: int = 0, a: int = 0, b: int = 0):
    return 0.5 * height * (a + b)
h = int(input("height: "))
a = int(input("first base: "))
b = int(input("second base: "))
print(trapezoidArea(h, a, b))