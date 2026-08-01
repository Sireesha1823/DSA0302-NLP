words = input("Enter words separated by space: ").split()

print("\nWord\t\tStem")

for word in words:
    if word == "relational":
        stem = "relat"
    elif word == "relation":
        stem = "relat"
    elif word == "relate":
        stem = "relat"
    else:
        stem = word

    print(word, "\t", stem)
