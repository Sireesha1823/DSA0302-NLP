from collections import Counter
import math

train = """
the student is studying
the student is learning
the student is reading
the teacher is teaching
"""

test = """
the student is learning
"""

train_words = train.lower().split()
test_words = test.lower().split()

# Unigram
unigram = Counter(train_words)

# Bigram
bigram = Counter(
    zip(train_words, train_words[1:])
)

# Trigram
trigram = Counter(
    zip(train_words, train_words[1:], train_words[2:])
)

# Entropy
total = len(train_words)
entropy = 0

for word, count in unigram.items():
    probability = count / total
    entropy -= probability * math.log2(probability)

print("Unigram Entropy:",
      round(entropy, 3))

print("\nBigram Probabilities:")

for pair, count in bigram.items():
    probability = count / unigram[pair[0]]
    print(pair, "=", round(probability, 3))

print("\nTest Sentence:")
print("the student is learning")

if ("is", "learning") in bigram:
    print("The sequence is predictable.")
else:
    print("The sequence is not found.")
