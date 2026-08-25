def check_agreement(sentence):
    words = sentence.lower().split()

    if len(words) != 3:
        return False

    subject = words[0]
    verb = words[1]
    noun = words[2]

    # Singular agreement
    if subject in ["he", "she", "it"] and verb.endswith("s"):
        return True

    # Plural agreement
    if subject in ["i", "you", "we", "they"] and not verb.endswith("s"):
        return True

    return False


sentence = input("Enter a sentence: ")

if check_agreement(sentence):
    print("Sentence has correct agreement.")
else:
    print("Sentence has incorrect agreement.")