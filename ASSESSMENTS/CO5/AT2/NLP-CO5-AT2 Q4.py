semantic_input = {
    "Action": "Buy",
    "Agent": "Student",
    "Object": "Book",
    "Tense": "Past"
}

print("Semantic Representation:")
for key, value in semantic_input.items():
    print(key, ":", value)

# Lexical selection
agent = "student"
action = "bought"
obj = "book"

# Surface realization
sentence = "The " + agent + " " + action + " a " + obj + "."

print("\nLexical Selection:")
print("Student -> student")
print("Buy -> bought")
print("Book -> book")

print("\nSurface Structure:")
print("Subject + Verb + Object")

print("\nGenerated Sentence:")
print(sentence)

# Validation
if sentence == "The student bought a book.":
    print("\nValidation: Grammatically Correct")
else:
    print("\nValidation: Needs Correction")
