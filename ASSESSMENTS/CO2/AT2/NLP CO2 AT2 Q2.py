words = ["disagree", "agreement", "agreeable"]

for word in words:
    if word == "disagree":
        prefix = "dis-"
        root = "agree"
        suffix = "-"
        transform = "Derivational"
        meaning = "Opposite of agree"
        normalized = "agree"

    elif word == "agreement":
        prefix = "-"
        root = "agree"
        suffix = "-ment"
        transform = "Derivational"
        meaning = "State of agreeing"
        normalized = "agree"

    elif word == "agreeable":
        prefix = "-"
        root = "agree"
        suffix = "-able"
        transform = "Derivational"
        meaning = "Able or willing to agree"
        normalized = "agree"

    print("Original Word :", word)
    print("Prefix        :", prefix)
    print("Root Word     :", root)
    print("Suffix        :", suffix)
    print("Type          :", transform)
    print("Meaning       :", meaning)
    print("Normalized    :", normalized)
    print("-" * 40)
