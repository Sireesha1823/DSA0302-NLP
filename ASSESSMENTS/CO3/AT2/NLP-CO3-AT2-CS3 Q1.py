# Q9: Transformation-Based Tagging

words = ["economic", "growth", "increases", "employment"]
tags = ["JJ", "NN", "NNS", "NN"]

print("Initial POS Tags:")
for word, tag in zip(words, tags):
    print(word + "/" + tag)

# Transformation rule:
# Change NNS to VBZ if preceding word is NN

for i in range(1, len(tags)):
    if tags[i] == "NNS" and tags[i - 1] == "NN":
        tags[i] = "VBZ"

print()
print("After Applying Transformation Rule:")
for word, tag in zip(words, tags):
    print(word + "/" + tag)
