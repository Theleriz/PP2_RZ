import re
def match_a_b2(string):
    return bool(re.fullmatch(r'ab{2,3}', string))