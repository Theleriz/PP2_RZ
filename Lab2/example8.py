target = 1000
number = 0
iterateIndex = 0
while number <= target:
    iterateIndex += 1
    number += iterateIndex ** 3
print("Cool, you just end the cycle.", number, iterateIndex)