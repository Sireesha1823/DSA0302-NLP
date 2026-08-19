# Q2: Top-Down Parsing and Earley Parsing
# No external libraries required

sentence = "John reads the book"

print("Original Sentence:")
print(sentence)

print()

# ---------------- TOP-DOWN PARSING ----------------

print("----- TOP-DOWN PARSING -----")

print("Start Symbol: S")

print("S")
print("|-- NP")
print("|   |-- John")
print("|")
print("|-- VP")
print("    |-- V -> reads")
print("    |")
print("    |-- NP")
print("        |-- Det -> the")
print("        |-- N -> book")

print()

# ---------------- EARLEY PARSING ----------------

print("----- EARLEY PARSING -----")

print("Step 1: Prediction")
print("S -> NP VP")

print()

print("Step 2: Scanning")
print("NP -> John")

print()

print("Step 3: Prediction")
print("VP -> V NP")

print()

print("Step 4: Scanning")
print("V -> reads")

print()

print("Step 5: Prediction")
print("NP -> Det N")

print()

print("Step 6: Scanning")
print("Det -> the")
print("N -> book")

print()

print("----- EARLEY PARSE TREE -----")

print("S")
print("|-- NP")
print("|   |-- John")
print("|")
print("|-- VP")
print("    |-- V -> reads")
print("    |")
print("    |-- NP")
print("        |-- Det -> the")
print("        |-- N -> book")

print()

print("----- RESULT -----")

print("Top-Down parsing starts from the start symbol.")
print("Earley parsing uses prediction, scanning and completion.")
print("Earley parsing is suitable for incomplete and ambiguous input.")
