import random

pos_tags = {
    "I": ["PRP"],
    "eat": ["VB", "NN"],
    "apple": ["NN"],
    "today": ["NN", "RB"]
}

sentence = input("Enter a sentence: ").split()

print("POS Tags:")

for word in sentence:
    if word in pos_tags:
        tag = random.choice(pos_tags[word])
    else:
        tag = "NN"

    print(word, "->", tag)