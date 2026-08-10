pos_dictionary = {
    "the": "DT",
    "a": "DT",
    "student": "NN",
    "teacher": "NN",
    "book": "NN",
    "python": "NNP",
    "is": "VBZ",
    "reads": "VBZ",
    "studies": "VBZ",
    "learning": "VBG",
    "good": "JJ",
    "beautiful": "JJ",
    "quickly": "RB",
    "in": "IN",
    "on": "IN",
    "and": "CC",
    "he": "PRP",
    "she": "PRP"
}

sentence = input("Enter a sentence: ").lower()

words = sentence.split()

print("\nPOS Tags:")

for word in words:

    if word in pos_dictionary:
        tag = pos_dictionary[word]

    elif word.endswith("ing"):
        tag = "VBG"

    elif word.endswith("ly"):
        tag = "RB"

    elif word.endswith("ed"):
        tag = "VBD"

    else:
        tag = "NN"

    print(word, "->", tag)
