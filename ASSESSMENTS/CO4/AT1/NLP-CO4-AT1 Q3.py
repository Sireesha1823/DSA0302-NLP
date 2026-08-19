def word_sense_disambiguation(query):

    query = query.lower()

    if "apple accessories" in query:
        return "Technology Brand"

    elif "mouse wireless" in query:
        return "Computer Device"

    elif "java tutorial" in query:
        return "Programming Language"

    elif "python course" in query:
        return "Programming Language"

    else:
        return "Sense Not Found"


# Input
query = input("Enter search query: ")

# Output
sense = word_sense_disambiguation(query)

print("Selected Word Sense:", sense)
