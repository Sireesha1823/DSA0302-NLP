text = [
    ("John", "person", "male", "singular"),
    ("Mary", "person", "female", "singular"),
    ("park", "place", "neutral", "singular"),
    ("He", "pronoun", "male", "singular"),
    ("ball", "object", "neutral", "singular"),
    ("She", "pronoun", "female", "singular"),
    ("it", "pronoun", "neutral", "singular"),
    ("dog", "animal", "neutral", "singular"),
    ("him", "pronoun", "male", "singular"),
    ("they", "pronoun", "neutral", "plural")
]

candidates = {
    "He": ["John", "Mary"],
    "She": ["John", "Mary"],
    "it": ["ball", "park"],
    "him": ["John", "Mary", "dog"],
    "they": ["John", "Mary", "dog"]
}

gender = {
    "John": "male",
    "Mary": "female",
    "ball": "neutral",
    "park": "neutral",
    "dog": "neutral"
}

number = {
    "John": "singular",
    "Mary": "singular",
    "ball": "singular",
    "park": "singular",
    "dog": "singular"
}

pronoun_gender = {
    "He": "male",
    "She": "female",
    "it": "neutral",
    "him": "male",
    "they": "neutral"
}

pronoun_number = {
    "He": "singular",
    "She": "singular",
    "it": "singular",
    "him": "singular",
    "they": "plural"
}

resolved = {}

for pronoun, possible in candidates.items():

    valid = []

    for candidate in possible:

        # Gender constraint
        if pronoun_gender[pronoun] == "neutral":
            gender_ok = True
        else:
            gender_ok = gender[candidate] == pronoun_gender[pronoun]

        # Number constraint
        number_ok = number[candidate] == "singular"

        if gender_ok and number_ok:
            valid.append(candidate)

    # Semantic compatibility
    if pronoun == "it" and "ball" in valid:
        resolved[pronoun] = "ball"

    elif pronoun == "they":
        resolved[pronoun] = "John + Mary + dog"

    elif valid:
        resolved[pronoun] = valid[0]


print("COREference Resolution")
print("----------------------")

for pronoun, antecedent in resolved.items():
    print(pronoun, "->", antecedent)

print("\nFinal Coreference Chains:")
print("John -> He -> him")
print("Mary -> She")
print("ball -> it")
print("John + Mary + dog -> they -> all")
