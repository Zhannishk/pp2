import re

with open('row.txt', 'r') as file:
    txt = file.read()

#1
matches = re.findall('ab*', txt)
print(matches)

# 2
matches = re.findall('abb?', txt)
print(matches)

# 3
sequence = re.findall('[a-z]+_[a-z]+', txt)
print(sequence)

# 4
sequence = re.findall('[A-Z][a-z]+', txt)
print(sequence)

# 5
matches = re.findall('a.*b$', txt)
print(matches)

# 6
x = re.sub('[ ,.]', ':', txt)
print(x)

# 7

# 8
x = re.findall('[A-Z][^A-Z]*', txt)
print(x)

# 9
x = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)
print(x)

# 10