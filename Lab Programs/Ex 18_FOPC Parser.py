import re

expression = input("Enter a logical expression: ")

pattern = r'([A-Za-z]+)\(([^()]*)\)'

matches = re.findall(pattern, expression)

if matches:
    print("Valid FOPC expression")
    for predicate, arguments in matches:
        print("Predicate:", predicate)
        print("Arguments:", arguments)
else:
    print("Invalid FOPC expression")