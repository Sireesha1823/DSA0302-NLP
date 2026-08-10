from collections import Counter

text = """
the student is studying
the student is learning
the student is reading
the student is writing
the teacher is teaching
"""

words = text.lower().split()

unigram = Counter(words)
bigram = Counter(zip(words, words[1:]))
trigram = Counter(zip(words, words[1:], words[2:]))

def predict(w1, w2):

    results = []

    # Trigram
    for (a, b, c), count in trigram.items():
        if a == w1 and b == w2:
            probability = count / bigram[(a, b)]
            results.append((c, probability))

    if results:
        print("\nUsing Trigram")
        return results

    # Bigram
    for (a, b), count in bigram.items():
        if a == w2:
            probability = count / unigram[a]
            results.append((b, probability))

    if results:
        print("\nTrigram not found")
        print("Using Bigram")
        return results

    # Unigram
    print("\nTrigram and Bigram not found")
    print("Using Unigram")

    total = len(words)

    return [(word, count / total)
            for word, count in unigram.items()]


w1 = input("Enter first word: ").lower()
w2 = input("Enter second word: ").lower()

result = predict(w1, w2)

result.sort(key=lambda x: x[1], reverse=True)

print("\nTop Predictions:")

for word, probability in result[:5]:
    print(word, ":", round(probability, 2))
