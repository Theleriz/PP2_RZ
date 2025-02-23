import re
def camelToSnake(string):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', string).lower()