import re
def matchAanyB(string):
    return bool(re.fullmatch(r'a.*b', string))