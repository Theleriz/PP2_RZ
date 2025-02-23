import re
def replaceColon(string):
    return re.sub(r'[ ,.]', ':', string)