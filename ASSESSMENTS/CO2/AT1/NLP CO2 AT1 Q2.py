words = input("Enter words separated by space: ").split()

print("\nWord\t\tRoot\t\tPrefix\tSuffix")

for word in words:
    if word == "unhappy":
        print(word, "\thappy\tun\t-")
    elif word == "happiness":
        print(word, "\thappy\t-\tness")
    elif word == "happily":
        print(word, "\thappy\t-\tly")
