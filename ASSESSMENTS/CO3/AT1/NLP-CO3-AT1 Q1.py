from collections import Counter

text = """
the student is studying
the student is learning
the student is reading
the student is writing
the student is studying python
the teacher is teaching
"""

words = text.lower().split()

# Unigram
unigram = Counter(words)

# Bigram
bigram = Counter(zip(words, words[1:]))

# Trigram
trigram = Counter(zip(words, words[1:], words[2:]))

print("Unigram:", unigram)
print("Bigram:", bigram)
print("Trigram:", trigram)

# Input
sentence = input("Enter sentence: ").lower().split()

# Bigram prediction
last_word = sentence[-1]

predictions = []

for (w1, w2), count in bigram.items():
    if w1 == last_word:
        probability = count / unigram[w1]
        predictions.append((w2, probability))

predictions.sort(key=lambda x: x[1], reverse=True)

print("\nTop Next Word Predictions:")

for word, probability in predictions[:5]:
    print(word, ":", round(probability, 2))

# Unseen bigram
print("\nUnseen N-gram probability:")

if ("student", "computer") not in bigram:
    print("P(computer | student) = 0")
