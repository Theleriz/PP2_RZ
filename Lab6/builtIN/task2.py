import string as st
def CountLetters(string: str):
    numberOfUpper = 0
    numberOfLower = 0
    for i in string:
        if i in st.ascii_uppercase:
            numberOfUpper += 1
        elif i in st.ascii_lowercase:
            numberOfLower += 1
    return [numberOfUpper, numberOfLower]
print(f"Number of capital: {CountLetters('Hello World')[0]} \nNumber of lower: {CountLetters('Hello World')[1]}")