sentence = [
    ("I", "PRP"),
    ("play", "NN"),
    ("cricket", "NN")
]

print("Before Transformation:")
print(sentence)

new_sentence = []

for word, tag in sentence:
    if word == "play":
        tag = "VB"

    new_sentence.append((word, tag))

print("\nAfter Transformation:")
print(new_sentence)