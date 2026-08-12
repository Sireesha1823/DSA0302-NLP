# Q3: Deleted Interpolation

# Given counts
count_data_science_is = 1
count_data_science = 3

count_science_is = 2
count_science = 3

count_is = 2
total_words = 15

# Calculate probabilities
trigram = count_data_science_is / count_data_science
bigram = count_science_is / count_science
unigram = count_is / total_words

# Interpolation weights
lambda1 = 0.5
lambda2 = 0.3
lambda3 = 0.2

# Deleted interpolation
probability = (
    lambda1 * trigram +
    lambda2 * bigram +
    lambda3 * unigram
)

print("Trigram Probability =", trigram)
print("Bigram Probability =", bigram)
print("Unigram Probability =", unigram)

print()
print("Deleted Interpolation Probability =", probability)
print("Percentage =", probability * 100, "%")
