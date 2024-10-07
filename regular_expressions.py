import re
"""Lesson 1: Basic regular expressions"""
wzor = r"banan"
tekst = r"gruszkabananjabłko"
# match - searches until it finds first match
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
    # group() returns the part of the string where there was a match
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

# [] matches any character inside the brackets
# [A-Z] matches any uppercase letter
# [a-z] matches any lowercase letter
# [A-Za-z] matches any letter
# [^A-Za-z] matches any character that is not a letter -> ^ negates the class that was defined in the brackets
if re.match('^[rR]ok[-_=][0-9][0-9][0-9][0-9]$', "Rok-1994"):
    print("Dopasowano!")
else:
    print("Nie dopasowano")

"""Lesson 3: Repetitions"""
# * matches 0 or more repetitions of the preceding regex
if re.match("[A-Z][a-z]a*$", "A"):
    print("Dopasowano!")
else:
    print("Nie dopasowano")

# + matches 1 or more repetitions of the preceding regex
if re.match("[A-Z][a-z]a+$", "Alaaaaaa"):
    print("Dopasowano!")
else:
    print("Nie dopasowano")

# ? matches 0 or 1 repetition of the preceding regex
if re.match("[A-Z][a-z]?[A-Z]$", "AA"):
    print("Dopasowano!")
else:
    print("Nie dopasowano")

# {a, b} matches exactly from a to b repetitions of the preceding regex
# {, b} matches 0 to b repetitions of the preceding regex
if re.match("[A-Z][a-z]{2,5}$", "Aleksandra"):
    print("Dopasowano!")
else:
    print("Nie dopasowano")

"""Lesson 4: groups , email validation"""
# () creates a group
# space is important here - there is a space after the first group
wynik = re.match(r"^(Hello)( World)+$", "Hello World World World")

if wynik:
    print("Dopasowano!")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    # groups() returns a tuple with all the groups
    print(wynik.groups())
else:
    print("Nie dopasowano")
# give a group a name with (?P<name>)
# (:?...) is a non-capturing group - it doesn't create a group - it doesn't affect index numeration
# (|...) is an optional group
# (!|\.) means that the string must end with an exclamation mark or a dot
wynik = re.match(r"^((?:He)(?P<first>ll)o)( World)+(!|\.)$", "Hello World World World!")

if wynik:
    print("Dopasowano!")
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.group(3))
    # you can call a group by its name
    print(wynik.group("first"))
else:
    print("Nie dopasowano")

if re.match("^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9-\.]+[A-Za-z0-9])\.[A-Za-z0-9]+$", "b.a@p.pl"):
    print("Dopasowano!")
else:
    print("Nie dopasowano")