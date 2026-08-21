conversation = [
    ("User", "Can you book a train ticket for me?"),
    ("Agent", "Sure, where would you like to travel?"),
    ("User", "I want to go to Chennai."),
    ("Agent", "Your ticket has been booked.")
]

def identify_dialogue_act(sentence):
    sentence_lower = sentence.lower()

    if "can you" in sentence_lower or "please" in sentence_lower:
        return "Request"

    elif sentence.endswith("?"):
        return "Question"

    elif "ticket has been booked" in sentence_lower:
        return "Confirmation"

    else:
        return "Inform"


print("Dialogue Act Recognition\n")

acts = []

for speaker, sentence in conversation:
    act = identify_dialogue_act(sentence)
    acts.append(act)

    print(speaker + ": " + sentence)
    print("Dialogue Act:", act)
    print()

print("Dialogue Act Sequence:")
print(" -> ".join(acts))
