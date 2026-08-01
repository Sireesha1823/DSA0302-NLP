words = input("Enter words separated by space: ").split()

print("\nWord\t\tRoot\t\tType")

for word in words:
    if word.endswith("ed"):
        print(word, "\tconnect\tInflectional")
    elif word.endswith("ing"):
        print(word, "\tconnect\tInflectional")
    elif word.endswith("ion"):
        print(word, "\tconnect\tDerivational")
