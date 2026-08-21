source_sentence = "The boy is playing football."

print("Source Sentence:")
print(source_sentence)

# Step 1: Source analysis
subject = "boy"
action = "play"
object_word = "football"
tense = "present"
aspect = "progressive"

print("\nStep 1: Source Analysis")
print("Subject:", subject)
print("Action:", action)
print("Object:", object_word)
print("Tense:", tense)
print("Aspect:", aspect)

# Step 2: Interlingua representation
interlingua = {
    "ACTION": "PLAY",
    "AGENT": "BOY",
    "OBJECT": "FOOTBALL",
    "TENSE": "PRESENT",
    "ASPECT": "PROGRESSIVE"
}

print("\nStep 2: Interlingua Representation")
for key, value in interlingua.items():
    print(key, "=", value)

# Step 3: Candidate translations
candidates = {
    "Candidate 1": "అబ్బాయి ఫుట్‌బాల్ ఆడుతున్నాడు.",
    "Candidate 2": "బాలుడు ఫుట్‌బాల్ ఆడుతున్నాడు.",
    "Candidate 3": "అబ్బాయి ఫుట్‌బాల్ ఆడతాడు."
}

print("\nStep 3: Candidate Translations")
for key, value in candidates.items():
    print(key + ":", value)

# Step 4: Statistical scores
scores = {
    "Candidate 1": 0.846,
    "Candidate 2": 0.792,
    "Candidate 3": 0.434
}

print("\nStep 4: Statistical Scores")

for candidate, score in scores.items():
    print(candidate, ":", score)

# Select highest scoring translation
best_candidate = max(scores, key=scores.get)

# Step 5: Final translation
final_translation = candidates[best_candidate]

print("\nStep 5: Final Translation")
print(final_translation)

print("\nSelected:", best_candidate)
print("Highest Score:", scores[best_candidate])
