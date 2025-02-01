def histogram(lst: list):
    for i in lst:
        string = ''
        for j in range(0, i):
            string += '*'
        print(string)

histogram([4, 9, 7])