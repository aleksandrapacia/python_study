import re
"""Lesson 1: Basic regular expressions"""
wzor = r"banan"
tekst = r"gruszkabananjabłko"
# mathc - searches until it finds first match
# asterix (*) means that there can be any number of characters before and after the pattern
if re.match(r".*" + wzor + r".*", tekst):
    print("Dopasowano!")
else:
    print("Nie dopasowano")
# search - searches the whole text
if re.search(wzor, tekst):
    print("Dopasowano!")
else:
    print("Nie dopasowano")

print(re.findall(wzor, tekst))

dopasowanie = re.search(wzor, tekst)

if dopasowanie:
    # group() returns the part of the string where there was
    print(dopasowanie.group())
    # start() and end() methods return the start and end index of the first match
    print(dopasowanie.start())
    print(dopasowanie.end())
    # span() returns both start and end indexes
    print(dopasowanie.span())
# r = raw string
# sub() method replaces the matches with a string of your choice
tekst2 = re.sub(wzor, r"jagoda", tekst)
print(tekst2)
# dot (.) matches any character except a newline
# $ matches the end of the string
# ^ matches the beginning of the string
"""Lesson 2: Classes of signs, compartments"""
if re.match("^ko.$", "kot"):
    print("Dopasowano!")
else:
    print("Nie dopasowano")