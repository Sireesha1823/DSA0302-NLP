words = ["create", "creates", "creating"]

for word in words:
    if word == "create":
        suffix = "-"
        category = "Base Form"
        root = "create"
        normalized = "create"

    elif word == "creates":
        suffix = "-s"
        category = "Third Person Singular"
        root = "create"
        normalized = "create"

    elif word == "creating":
        suffix = "-ing"
        category = "Present Participle"
        root = "create"
        normalized = "create"

    print("Original Word      :", word)
    print("Suffix             :", suffix)
    print("Grammatical Form   :", category)
    print("Root Word          :", root)
    print("Normalized Form    :", normalized)
    print("-" * 40)
