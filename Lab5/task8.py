import re
def splitUppercase(string):
    return re.split(r'(?=[A-Z])', string)