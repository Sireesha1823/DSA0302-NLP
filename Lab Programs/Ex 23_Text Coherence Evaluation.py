import re
from collections import Counter


# Function to tokenize a sentence
def get_words(sentence):
    return re.findall(r'\b[a-zA-Z]+\b', sentence.lower())


# Function to calculate word overlap between two sentences
def word_overlap(sentence1, sentence2):
    words1 = set(get_words(sentence1))
    words2 = set(get_words(sentence2))

    if not words1 or not words2:
        return 0

    common_words = words1.intersection(words2)

    return len(common_words) / min(len(words1), len(words2))


# Function to evaluate coherence
def evaluate_coherence(text):
    sentences = re.split(r'[.!?]+', text)

    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) < 2:
        return 0

    scores = []

    for i in range(len(sentences) - 1):
        score = word_overlap(sentences[i], sentences[i + 1])
        scores.append(score)

    return sum(scores) / len(scores)


# Input
text = input("Enter a text: ")

# Calculate coherence score
score = evaluate_coherence(text)

print("\nText Coherence Evaluation")
print("----------------------------")
print("Coherence Score:", round(score, 2))

# Display interpretation
if score >= 0.5:
    print("Coherence Level: High")
elif score >= 0.2:
    print("Coherence Level: Moderate")
else:
    print("Coherence Level: Low")