words = input("Enter words separated by space: ").split()

print("\nWord\t\tRoot\t\tType")

for word in words:
    if word == "writes":
        print(word, "\twrite\tRegular")
    elif word == "writing":
        print(word, "\twrite\tRegular")
    elif word == "written":
        print(word, "\twrite\tIrregular")
