def inflect(word):
    print("\nRoot Word:", word)

    # Present Tense
    if word.endswith('y'):
        present = word[:-1] + "ies"
    else:
        present = word + "s"

    # Present Continuous
    if word.endswith('e'):
        present_cont = word[:-1] + "ing"
    else:
        present_cont = word + "ing"

    # Past Tense
    if word.endswith('e'):
        past = word + "d"
    else:
        past = word + "ed"

    print("Simple Present (3rd Person):", present)
    print("Present Continuous:", present_cont)
    print("Past Tense:", past)


word = input("Enter a root word: ")
inflect(word)
