# Q1 - Banking Customer Support Chatbot
# No external libraries required

sentence = "Show me the transactions with the card from last month"

print("========== BANKING CHATBOT ==========")

print("\nInput:")
print(sentence)

# ------------------------------------------------
# 1. AMBIGUITY ANALYSIS
# ------------------------------------------------

print("\n========== AMBIGUITY ANALYSIS ==========")

print("The sentence contains structural ambiguity.")

print("\nInterpretation 1:")
print("Show the transactions that were made using the card")
print("and that occurred during last month.")

print("\nInterpretation 2:")
print("The phrase 'from last month' may be attached")
print("to a different part of the sentence.")

# ------------------------------------------------
# 2. CFG REPRESENTATION
# ------------------------------------------------

print("\n========== CFG REPRESENTATION ==========")

print("S -> VP")
print("VP -> V NP")
print("NP -> DET NOUN PP PP")
print("PP -> PREP NP")
print("NP -> DET NOUN")

print("\nGrammar interpretation:")
print("S")
print("|-- VP")
print("    |-- V -> show")
print("    |-- NP -> the transactions")
print("        |-- PP -> with the card")
print("        |-- PP -> from last month")

# ------------------------------------------------
# 3. SEMANTIC REPRESENTATION
# ------------------------------------------------

print("\n========== SEMANTIC REPRESENTATION ==========")

intent = "SHOW_TRANSACTIONS"
object_name = "TRANSACTIONS"
instrument = "CARD"
time_period = "LAST_MONTH"

print("Intent      :", intent)
print("Object      :", object_name)
print("Instrument  :", instrument)
print("Time        :", time_period)

# ------------------------------------------------
# 4. PCFG
# ------------------------------------------------

print("\n========== PCFG ==========")

print("Example probabilistic grammar rules:")

print("NP -> DET NOUN PP PP     Probability = 0.60")
print("NP -> DET NOUN           Probability = 0.40")
print("PP -> PREP NP            Probability = 1.00")

print("\nPCFG selects the most probable interpretation")
print("when multiple parse structures are possible.")

# ------------------------------------------------
# 5. FEATURE STRUCTURE
# ------------------------------------------------

print("\n========== FEATURE STRUCTURE ==========")

print("Subject/Object Features:")
print("Number : Plural")
print("Person : Third")
print("Category : Noun")

# ------------------------------------------------
# 6. FINAL RESULT
# ------------------------------------------------

print("\n========== FINAL RESULT ==========")

print("The chatbot interprets the query as:")

print("SHOW the TRANSACTIONS")
print("made using the CARD")
print("during LAST MONTH.")

print("\nImproved approach:")
print("CFG + PCFG + Feature Structures + Earley Parsing")
