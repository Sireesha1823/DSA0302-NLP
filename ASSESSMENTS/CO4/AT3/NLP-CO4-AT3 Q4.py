print("===== FEATURE STRUCTURES =====")
subject = {
    "person": 3,
    "number": "singular"
}
verb = {
    "person": 3,
    "number": "singular"
}
print("Subject Features:")
print(subject)

print()

print("Verb Features:")
print(verb)

print()
if subject["person"] == verb["person"] and subject["number"] == verb["number"]:
    print("Subject-Verb Agreement: CORRECT")
else:
    print("Subject-Verb Agreement: INCORRECT")
print()
print("===== SUBCATEGORIZATION FRAMES =====")
verb_frames = {
    "eat": ["Subject", "Object"],
    "sleep": ["Subject"],
    "give": ["Subject", "Object", "Indirect Object"],
    "read": ["Subject", "Object"]
}
selected_verb = "eat"

print("Verb:", selected_verb)

print("Required Arguments:")
print(verb_frames[selected_verb])

print()
sentence_arguments = ["Subject", "Object"]

print("Sentence Arguments:")
print(sentence_arguments)

print()

if sentence_arguments == verb_frames[selected_verb]:
    print("Argument Structure: CORRECT")
else:
    print("Argument Structure: INCORRECT")
print()
print("===== EXAMPLE =====")
print("Sentence: The boy eats an apple.")
print()

print("Subject: boy")
print("Verb: eats")
print("Object: apple")

print()

print("Feature Structure:")
print("Subject -> Number = Singular")
print("Verb -> Number = Singular")

print()

print("Subcategorization:")
print("eat -> Subject + Object")

print()

print("===== RESULT =====")

print("Feature structures check grammatical features")
print("such as person and number.")

print()

print("Subcategorization frames specify the")
print("arguments required by a verb.")
