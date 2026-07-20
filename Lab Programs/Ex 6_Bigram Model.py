import random

text = "machine learning is fun machine learning is useful"

words = text.split()

bigrams = {}

for i in range(len(words) - 1):
    key = words[i]
    value = words[i + 1]

    if key not in bigrams:
        bigrams[key] = []

    bigrams[key].append(value)

word = random.choice(words)
sentence = [word]

for i in range(10):
    if word in bigrams:
        word = random.choice(bigrams[word])
        sentence.append(word)
    else:
        break

print("Generated Text:")
print(" ".join(sentence))