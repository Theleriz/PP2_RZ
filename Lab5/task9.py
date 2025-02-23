import re
def insertSpaces(string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', string)