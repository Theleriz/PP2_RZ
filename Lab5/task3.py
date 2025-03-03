import re
def findSnakeCaseWords(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)


