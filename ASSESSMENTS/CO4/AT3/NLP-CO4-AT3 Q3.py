sentence = "She saw the man with a telescope"

print("Original Sentence:")
print(sentence)

print()

print("----- CFG PARSING -----")

print("CFG generates possible sentence structures.")

print()

print("Interpretation 1:")
print("She [saw the man] [with a telescope]")
print("Meaning: She used a telescope to see the man.")

print()

print("Interpretation 2:")
print("She [saw [the man with a telescope]]")
print("Meaning: The man had a telescope.")

print()


print("----- PCFG PARSING -----")

print("PCFG assigns probabilities to different")
print("possible parse structures.")

interpretation1_probability = 0.70
interpretation2_probability = 0.30

print()

print("Interpretation 1 Probability:",
      interpretation1_probability)

print("Interpretation 2 Probability:",
      interpretation2_probability)

print()

if interpretation1_probability > interpretation2_probability:
    print("PCFG selects Interpretation 1")
else:
    print("PCFG selects Interpretation 2")

print()

print("----- NEURAL PARSING -----")

print("Neural parsing uses learned language patterns")
print("and contextual information.")

print()

print("Input:")
print(sentence)

print()

print("Neural Parser Analysis:")
print("The parser considers the context of the sentence.")

print()

print("Selected Interpretation:")
print("She used a telescope to see the man.")

print()

print("----- COMPARISON -----")

print("CFG:")
print("Generates possible grammatical structures.")

print()

print("PCFG:")
print("Assigns probabilities to possible structures.")

print()

print("Neural Parsing:")
print("Uses learned contextual information to resolve ambiguity.")

print()


print("----- RESULT -----")

print("CFG can identify multiple interpretations.")
print("PCFG can rank interpretations using probabilities.")
print("Neural parsing can use contextual information")
print("to select the most suitable interpretation.")
