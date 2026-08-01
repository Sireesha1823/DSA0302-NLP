words = input("Enter words separated by space: ").split()

print("\nWord\t\tStem\t\tType")

for word in words:
    if word.endswith("ed"):
        print(word, "\tplay\tInflectional")
    elif word.endswith("er"):
        print(word, "\tplay\tDerivational")
    elif word.endswith("ing"):
        print(word, "\tplay\tInflectional")
