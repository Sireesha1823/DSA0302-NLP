# Q11: Corpus Frequency Analysis

frequency = {
    "economic": 120,
    "growth": 450,
    "increases": 210,
    "employment": 380
}

total = sum(frequency.values())

print("Total Word Frequency =", total)
print()

print("Word Frequency Distribution")
print("---------------------------")

for word, count in frequency.items():
    probability = count / total
    percentage = probability * 100

    print("Word:", word)
    print("Frequency:", count)
    print("Probability:", round(probability, 4))
    print("Percentage:", round(percentage, 2), "%")
    print()

most_frequent = max(frequency, key=frequency.get)

print("Most Frequent Word:", most_frequent)
print("Frequency:", frequency[most_frequent])
