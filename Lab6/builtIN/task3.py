def isPolindrom(string: str) -> bool:
    TruthList = []
    for i in range(len(string)):
        TruthList.append(string[i] == string[-i - 1])
    return all(TruthList)

print((isPolindrom("11111")))