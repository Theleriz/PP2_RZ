fruits = ("apple", "banana" , "cherry", "orange", "laim")
print(fruits)
print(fruits[1])
print(fruits[:1])

newFruits = list(fruits)
newFruits.append("kiwi")
newFruits = tuple(newFruits)
print(newFruits)

colorsHEX = ("3A5683", "2708A0", "639A88") 
(ylnmBLue, dukeBlue, zomp) = colorsHEX
print(ylnmBLue, dukeBlue, zomp)

for HEX_of_color in colorsHEX:
    print(HEX_of_color)

newTuple = fruits + colorsHEX
print(newTuple)

print(fruits.count("banana"))