words = ["govern", "government", "governance"]

for word in words:
    if word == "govern":
        root = "govern"
        affix = "-"
        level = "Level 0 (Root)"
        normalized = "govern"

    elif word == "government":
        root = "govern"
        affix = "-ment"
        level = "Level 1 (Derivational)"
        normalized = "govern"

    elif word == "governance":
        root = "govern"
        affix = "-ance"
        level = "Level 1 (Derivational)"
        normalized = "govern"

    print("Original Word      :", word)
    print("Root Word          :", root)
    print("Affix              :", affix)
    print("Derivational Level :", level)
    print("Normalized Form    :", normalized)
    print("-" * 40)
