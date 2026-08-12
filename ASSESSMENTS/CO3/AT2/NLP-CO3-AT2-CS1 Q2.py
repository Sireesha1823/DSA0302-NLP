# Q2: Backoff Model

# Trigram probability
trigram_probability = 0

# Bigram probability
bigram_probability = 0

# Unigram probability
unigram_probability = 0

print("Sequence: data science improves")
print()

print("Trying Trigram:")
print("P(improves | data, science) =", trigram_probability)

if trigram_probability == 0:
    print("Trigram unseen -> Backing off to Bigram")

print()
print("Trying Bigram:")
print("P(improves | science) =", bigram_probability)

if bigram_probability == 0:
    print("Bigram unseen -> Backing off to Unigram")

print()
print("Trying Unigram:")
print("P(improves) =", unigram_probability)

print()
print("Final estimated probability = 0")
print("Backoff is useful for handling unseen word sequences.")
