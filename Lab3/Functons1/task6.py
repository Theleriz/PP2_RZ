def reverseString():
    words = list(input().split())
    words = reversed(words)
    string = ""
    for i in words:
        string = string + i + " "
    print(string)