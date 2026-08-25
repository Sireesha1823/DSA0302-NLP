grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}

sentence = "the cat sees the dog".split()

def parse(symbol, words, position):
    if symbol not in grammar:
        if position < len(words) and symbol == words[position]:
            return position + 1
        return None

    for production in grammar[symbol]:
        current = position

        for item in production:
            result = parse(item, words, current)

            if result is None:
                break

            current = result
        else:
            return current

    return None

result = parse("S", sentence, 0)

if result == len(sentence):
    print("Sentence is accepted by the grammar.")
else:
    print("Sentence is rejected by the grammar.")