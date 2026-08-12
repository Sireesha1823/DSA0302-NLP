# Q12: Transformation-Based Tagging and Entropy

import math

# Initial probability distribution of possible tags
# Example probabilities for demonstrating entropy calculation
initial = {
    "NNS": 0.50,
    "VBZ": 0.30,
    "NN": 0.20
}

# After applying the transformation rule,
# confidence is concentrated on VBZ
after = {
    "VBZ": 1.0
}

def calculate_entropy(probabilities):
    entropy = 0

    for p in probabilities.values():
        if p > 0:
            entropy -= p * math.log2(p)

    return entropy

initial_entropy = calculate_entropy(initial)
after_entropy = calculate_entropy(after)

print("Initial Tag Distribution:")
for tag, probability in initial.items():
    print(tag, "=", probability)

print()
print("Initial Entropy =", round(initial_entropy, 4), "bits")

print()
print("After Transformation:")
for tag, probability in after.items():
    print(tag, "=", probability)

print()
print("After Transformation Entropy =", round(after_entropy, 4), "bits")

print()

if after_entropy < initial_entropy:
    print("Entropy decreased.")
    print("Tagging uncertainty decreased.")
    print("Tagging confidence increased.")
else:
    print("Entropy did not decrease.")
