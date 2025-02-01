from itertools import permutations


def perm() :
    string = input()
    stringPerm = list(permutations(string))
    print(stringPerm)
    for i in stringPerm:
        print(str(i))
