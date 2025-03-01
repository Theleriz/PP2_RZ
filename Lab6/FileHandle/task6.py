import string

for name in string.ascii_uppercase:
    fileName = f"{name}.txt"
    with open(fileName, 'w') as file:
        file.write(f"name")