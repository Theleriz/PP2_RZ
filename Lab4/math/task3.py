import math

def areOfPolygon(n, a):
    area = (n * (a ** 2)) / (math.tan(math.radians(180 / n)) * 4)
    return area

print(areOfPolygon(4, 25))