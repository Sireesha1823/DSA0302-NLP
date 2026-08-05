words = ["activate", "activation", "reactivation"]

for word in words:
    if word == "activate":
        prefix = "-"
        root = "activate"
        suffix = "-"
        sequence = "Root Word"
        meaning = "To make active"
        normalized = "activate"

    elif word == "activation":
        prefix = "-"
        root = "activate"
        suffix = "-ion"
        sequence = "activate + ion"
        meaning = "Process of becoming active"
        normalized = "activate"

    elif word == "reactivation":
        prefix = "re-"
        root = "activate"
        suffix = "-ion"
        sequence = "re + activate + ion"
        meaning = "To make active again"
        normalized = "activate"

    print("Original Word        :", word)
    print("Prefix              :", prefix)
    print("Root Word           :", root)
    print("Suffix              :", suffix)
    print("Derivational Sequence:", sequence)
    print("Meaning             :", meaning)
    print("Normalized Form     :", normalized)
    print("-" * 45)
