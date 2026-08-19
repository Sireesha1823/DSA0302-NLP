sentence = "The boy eats the apple"

print("Original Sentence:")
print(sentence)

print()

print("----- CFG TREE -----")

print("S")
print("|-- NP")
print("|   |-- Det -> The")
print("|   |-- N   -> boy")
print("|")
print("|-- VP")
print("    |-- V  -> eats")
print("    |")
print("    |-- NP")
print("        |-- Det -> the")
print("        |-- N   -> apple")

print()

print("----- DEPENDENCY PARSING -----")

print("eats -> subject -> boy")
print("eats -> object -> apple")
print("boy -> determiner -> The")
print("apple -> determiner -> the")

print()

print("----- RESULT -----")

print("CFG represents the sentence using a tree structure.")
print("Dependency parsing represents relationships between words.")
