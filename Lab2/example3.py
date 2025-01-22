fruits = ["apple", "banana", "orange"]
print(fruits)

stufList = [1, "fruit"]

print(stufList)
print(len(stufList))

print(stufList[1])
print(fruits[:2])

fruits.insert(3, "Lime")
fruits.append("cherry")
print(fruits)
stufList.extend(fruits)
print(stufList)

stufList.remove("banana")
stufList.pop(1)
print(stufList)

for i in stufList:
    order = 1
    print(i, ' ', i)
    order += 1
    
numbers = [x for x in range(10) if x % 2 ==0]
print(numbers)

listOfNumbers = [100, 50, 65, 82, 23]
listOfNumbers.sort(reverse = True)
print(listOfNumbers)

copyOfFruits = fruits.copy()
print(copyOfFruits)

print(type(stufList))