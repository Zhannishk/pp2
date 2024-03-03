import re

def upper(s):
    x = re.findall('[A-Z]', s)
    print(len(x))
def lower(s):
    x = re.findall('[a-z]', s)
    print(len(x))

s = input()
upper(s)
lower(s)