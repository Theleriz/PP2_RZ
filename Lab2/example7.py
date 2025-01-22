testTuple1 = ("apple", "banana", "cherry")
testTuple2 = ("kiwi", "laim", "melon")

if testTuple1 is testTuple2:
    print("Yes, this is the same object.")
elif testTuple2 is not testTuple2:
    print("No, this is not the same object.")
    for item1 in testTuple1:
        for item2 in testTuple2:
            if item1 == item2:
                print(f"But, we have same elements {item1}")
else:
    print("Nah, nothing is same.")

x = 10
y = 20
z = 30 
if x < y:
    if x > z:
        print("Three variable are not equal")
    elif x < z and y < z:
        print("Z bigger the x and y")
    