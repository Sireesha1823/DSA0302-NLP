sentence = "The bank by the river flooded after the storm, but it was saved by quick action."

print("SOURCE SENTENCE")
print(sentence)

print("\n1. WORD SENSE DISAMBIGUATION")
print("----------------------------")

possible_senses = [
    "Financial institution",
    "Riverbank"
]

print("Possible meanings:")
for sense in possible_senses:
    print("-", sense)

context = ["river", "flooded", "storm"]

if "river" in context and "flooded" in context:
    meaning = "Riverbank"
else:
    meaning = "Financial institution"

print("Selected meaning:", meaning)

print("\nReason:")
print("The words 'river' and 'flooded' support the riverbank meaning.")

print("\n2. PREDICATE LOGIC")
print("------------------")

print("RiverBank(b)")
print("River(r)")
print("LocatedBy(b,r)")
print("Storm(s)")
print("Flood(b)")
print("After(Flood(b),s)")
print("QuickAction(q)")
print("Saved(b,q)")

print("\n3. DISCOURSE RELATION")
print("---------------------")

print("Contrast(")
print("    Flood(b) AND After(Flood(b),s),")
print("    Saved(b,q)")
print(")")

print("\n4. DISCOURSE TREE")
print("-----------------")

print("                 CONTRAST")
print("                /        \\")
print("               /          \\")
print("        Clause 1          Clause 2")
print("           |                 |")
print("     Bank flooded       Bank saved")
print("     after storm        by quick action")

print("\n5. TARGET SENTENCE")
print("------------------")

target = "The riverbank flooded after the storm, but quick action helped save it."

print(target)

print("\n6. FINAL RESULT")
print("---------------")

print("Bank = Riverbank")
print("Discourse relation = Contrast")
print("All important entities and relations are preserved.")
