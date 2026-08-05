words = ["analyzing", "analysis", "analytical"]

for word in words:
    if word == "analyzing":
        root = "analyze"
        affix = "-ing"
        transform = "Inflectional"
        normalized = "analyze"

    elif word == "analysis":
        root = "analyze"
        affix = "-sis"
        transform = "Derivational"
        normalized = "analyze"

    elif word == "analytical":
        root = "analyze"
        affix = "-ical"
        transform = "Derivational"
        normalized = "analyze"

    print("Original Word :", word)
    print("Root Word     :", root)
    print("Affix         :", affix)
    print("Type          :", transform)
    print("Normalized    :", normalized)
    print("-" * 35)
