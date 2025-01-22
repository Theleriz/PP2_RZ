pointsRange = {
    90 : "A",
    80 : "B",
    70 : "C",
    60 : "D",
    50 : "F"
}

print(pointsRange.keys())
print(pointsRange.values())
print(pointsRange[90])


pointsRange[90] = "A+"
pointsRange.update({80: "B+"})
print(pointsRange)

pointsRange[20] = "Fx"
pointsRange.update({19 : "Retake"})
print(pointsRange)

pointsRange.pop(20)

for point, grade in pointsRange.items():
    print(point, grade)

newDict = pointsRange.copy()



firstName = {
    1 : "Adam",
    2 : "Brad",
    3 : "Oscar",
    4 : "Jon",
}

secondName = {
    1 : "Smith",
    2 : "Pitt",
    3 : "Wilde",
    4 : "Jones"
}

fullName = {
    "first name" : firstName,
    "second name" : secondName
}
print(fullName)
