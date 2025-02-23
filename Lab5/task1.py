import re
def match_a_b(string):
    return bool(re.fullmatch(r'ab*', string))