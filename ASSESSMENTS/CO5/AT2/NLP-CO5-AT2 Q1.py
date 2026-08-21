text = "Ravi met Arun at the library. He borrowed a book and later returned it."

entities = ["Ravi", "Arun", "book"]

pronoun1 = "He"
pronoun2 = "it"

# Reference resolution using discourse context
if pronoun1 == "He":
    antecedent1 = "Ravi"

if pronoun2 == "it":
    antecedent2 = "book"

resolved_text = (
    "Ravi met Arun at the library. "
    + antecedent1 +
    " borrowed a book and later returned the "
    + antecedent2 + "."
)

print("Original Text:")
print(text)

print("\nResolved Text:")
print(resolved_text)

print("\nResolution:")
print("He ->", antecedent1)
print("it ->", antecedent2)
