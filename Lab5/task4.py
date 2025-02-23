import re
def findCapitalWords(string):
    return re.findall(r'\b[A-Z][a-z]+\b', string)