sentences = [
    "The roads were flooded after heavy rainfall.",
    "Therefore, schools were closed for the day.",
    "Students attended classes online."
]

print("Discourse:")
for i, sentence in enumerate(sentences, 1):
    print("S" + str(i) + ":", sentence)

print("\nDiscourse Relations:")

print("S1 -> S2 : Cause and Effect")
print("S2 -> S3 : Result and Consequence")

print("\nDiscourse Structure:")
print("Heavy rainfall")
print("      ↓")
print("Roads were flooded")
print("      ↓")
print("Schools were closed")
print("      ↓")
print("Students attended classes online")

print("\nCoherence:")
print("The sentences are coherent because each event logically")
print("follows from the previous event.")
