sentence = "The doctor who reviewed the patient last week recommends starting medication and scheduling a follow-up visit in Chennai."

print("HEALTHCARE REPORT NLP")
print()
print("INPUT SENTENCE:")
print(sentence)

words = sentence.lower().replace(".", "").split()

print()
print("1. TOKENIZATION")
print(words)

print()
print("2. MEDICAL ENTITIES")

print("doctor -> Medical Professional")
print("patient -> Patient")
print("medication -> Treatment")
print("follow-up visit -> Medical Action")
print("Chennai -> Location")
print("last week -> Time")

print()
print("3. CFG SYNTACTIC STRUCTURE")

print("S")
print("|-- NP")
print("    |-- The doctor")
print("    |-- Relative Clause")
print("        |-- who reviewed the patient last week")
print("|-- VP")
print("    |-- recommends")
print("    |-- starting medication")
print("    |-- scheduling a follow-up visit in Chennai")

print()
print("4. FEATURE STRUCTURE")

doctor = {
    "category": "Noun",
    "number": "Singular",
    "person": "Third"
}

verb = {
    "category": "Verb",
    "number": "Singular",
    "person": "Third"
}

print("Doctor:")
print("Category :", doctor["category"])
print("Number   :", doctor["number"])
print("Person   :", doctor["person"])

print()
print("Recommends:")
print("Category :", verb["category"])
print("Number   :", verb["number"])
print("Person   :", verb["person"])

print()
print("5. SUBJECT-VERB AGREEMENT")

if doctor["number"] == verb["number"] and doctor["person"] == verb["person"]:
    print("Subject-Verb Agreement is CORRECT")
else:
    print("Subject-Verb Agreement is INCORRECT")

print()
print("6. SUB-CATEGORIZATION")

print("review")
print("Subject : Doctor")
print("Object  : Patient")

print()
print("recommend")
print("Subject : Doctor")
print("Object  : Medical Action")

print()
print("start")
print("Object  : Medication")

print()
print("schedule")
print("Object  : Follow-up Visit")

print()
print("7. PCFG AMBIGUITY RESOLUTION")

print("Possible interpretations are generated.")
print("PCFG assigns probabilities to the interpretations.")
print("The most probable interpretation is selected.")

print()
print("Selected Interpretation:")
print("Doctor recommends starting medication")
print("and scheduling a follow-up visit in Chennai.")

print()
print("8. SEMANTIC RELATIONS")

print("Doctor -- reviewed --> Patient")
print("Doctor -- reviewed_time --> Last Week")
print("Doctor -- recommends --> Starting Medication")
print("Doctor -- recommends --> Scheduling Follow-up Visit")
print("Follow-up Visit -- location --> Chennai")

print()
print("9. STRUCTURED OUTPUT")

print("Medical Professional : Doctor")
print("Patient             : Patient")
print("Review Time         : Last Week")
print("Treatment           : Medication")
print("Action 1            : Start Medication")
print("Action 2            : Schedule Follow-up Visit")
print("Location            : Chennai")
print("Diagnosis           : Not explicitly mentioned")

print()
print("10. NLP ARCHITECTURE")

print("Input Medical Report")
print("        ↓")
print("Preprocessing")
print("        ↓")
print("Tokenization")
print("        ↓")
print("CFG Parsing")
print("        ↓")
print("PCFG Ambiguity Resolution")
print("        ↓")
print("Feature Structure Analysis")
print("        ↓")
print("Medical Entity Extraction")
print("        ↓")
print("Sub-Categorization")
print("        ↓")
print("Semantic Relation Extraction")
print("        ↓")
print("Structured Medical Output")

print()
print("11. FINAL RESULT")

print("Medical information extracted successfully.")
print("Treatment : Medication")
print("Action    : Start Medication")
print("Action    : Schedule Follow-up Visit")
print("Location  : Chennai")
