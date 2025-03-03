import re
def snakeToCamel(string):
    words = string.split('_')
    finalWord = words[0] + ''.join(i.capitalize() for i in words[1:])
    return finalWord