# Q5: POS Tagging

sentence1 = {
    "Book": "VB",
    "a": "DT",
    "flight": "NN",
    "ticket": "NN",
    "now": "RB"
}

sentence2 = {
    "This": "DT",
    "book": "NN",
    "is": "VBZ",
    "interesting": "JJ"
}

print("Sentence 1:")
for word, tag in sentence1.items():
    print(word, "/", tag)

print()
print("Sentence 2:")
for word, tag in sentence2.items():
    print(word, "/", tag)

print()
print("In Sentence 1, 'book' is VB because it is an action/command.")
print("In Sentence 2, 'book' is NN because it refers to an object.")
