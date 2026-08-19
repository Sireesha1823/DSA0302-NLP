sentences = [
    "Doctor prescribed medicine to patient.",
    "Patient reported severe headache.",
    "Nurse monitored patient continuously.",
    "Medicine reduced blood pressure."
]

print("Syntax-Driven Semantic Analysis\n")

for sentence in sentences:

    print("Sentence:", sentence)

    words = sentence.replace(".", "").split()

    subject = words[0]
    verb = words[1]

    print("Subject:", subject)
    print("Verb:", verb)

    if subject.lower() == "doctor":
        print("Semantic Role: Doctor -> Agent")
        print("Medicine -> Theme/Object")
        print("Patient -> Recipient")

    elif subject.lower() == "patient":
        print("Semantic Role: Patient -> Experiencer")
        print("Headache -> Symptom")

    elif subject.lower() == "nurse":
        print("Semantic Role: Nurse -> Agent")
        print("Patient -> Object/Patient")

    elif subject.lower() == "medicine":
        print("Semantic Role: Medicine -> Cause/Agent")
        print("Blood Pressure -> Object")

    print()
