# Q10: POS Tag Error Analysis

words = ["economic", "growth", "increases", "employment"]

initial_tags = ["JJ", "NN", "NNS", "NN"]
correct_tags = ["JJ", "NN", "VBZ", "NN"]

print("POS Tag Analysis")
print("----------------")

for i in range(len(words)):
    print("Word:", words[i])
    print("Initial Tag:", initial_tags[i])
    print("Correct Tag:", correct_tags[i])

    if initial_tags[i] != correct_tags[i]:
        print("Status: Corrected")
    else:
        print("Status: Correct")

    print()

print("Sentence Structure:")
print("[NP Economic growth] [VP increases] [NP employment]")

print()
print("Reason:")
print("'growth' is a singular noun and acts as the subject.")
print("'increases' is the main verb and therefore receives VBZ.")
