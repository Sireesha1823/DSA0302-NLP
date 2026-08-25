def earley_parser(sentence):
    grammar = {
        'S': [['NP', 'VP']],
        'NP': [['Det', 'N']],
        'VP': [['V', 'NP']],
        'Det': [['the']],
        'N': [['cat'], ['dog']],
        'V': [['sees'], ['likes']]
    }

    words = sentence.split()

    for word in words:
        found = False

        for rule in grammar.values():
            for production in rule:
                if word in production:
                    found = True
                    break

        if not found:
            return False

    return True


sentence = input("Enter a sentence: ")

if earley_parser(sentence):
    print("Sentence accepted")
else:
    print("Sentence not accepted")