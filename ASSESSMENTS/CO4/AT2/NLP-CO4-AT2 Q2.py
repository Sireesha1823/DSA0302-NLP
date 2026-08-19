sentence = "Book a flight to Delhi with a window seat"

print("VOICE ASSISTANT - FLIGHT BOOKING")
print()
print("INPUT COMMAND:")
print(sentence)

words = sentence.lower().split()

print()
print("TOKENIZATION")
print(words)

intent = "BOOK FLIGHT"
destination = "DELHI"
seat_preference = "WINDOW"

print()
print("IMPORTANT INFORMATION")
print("Intent          :", intent)
print("Destination     :", destination)
print("Seat Preference :", seat_preference)

print()
print("AMBIGUITY ANALYSIS")
print("The phrase 'with a window seat' can create a prepositional phrase attachment ambiguity.")

print()
print("Possible Interpretation 1:")
print("Book a flight to Delhi and give the passenger a window seat.")

print()
print("Possible Interpretation 2:")
print("The phrase 'with a window seat' may be attached to the flight noun phrase.")

print()
print("POSSIBLE PARSE STRUCTURE")

print("S")
print("|-- VP")
print("    |-- V -> Book")
print("    |-- NP -> a flight")
print("    |-- PP -> to Delhi")
print("    |-- PP -> with a window seat")

print()
print("TOP-DOWN PARSING")
print("S")
print("↓")
print("VP")
print("↓")
print("V + NP")
print("↓")
print("Book + a flight")
print("↓")
print("to Delhi + with a window seat")

print()
print("LIMITATIONS OF TOP-DOWN PARSING")
print("1. It may require backtracking.")
print("2. Ambiguous input can create multiple choices.")
print("3. It may repeat parsing operations.")
print("4. It can be inefficient for complex input.")
print("5. It has limited support for incomplete commands.")
print("6. Backtracking can increase response time.")

print()
print("EARLEY PARSING")

print("PREDICT")
print("Predict possible grammar rules.")

print("SCAN")
print("Match the next word with the grammar.")

print("COMPLETE")
print("Complete the recognized grammatical structure.")

print()
print("EARLEY PARSING ADVANTAGES")
print("1. Handles ambiguous sentences.")
print("2. Handles complex CFG grammars.")
print("3. Stores intermediate parsing states.")
print("4. Reduces repeated computation.")
print("5. Handles partial input.")
print("6. Suitable for real-time applications.")
print("7. Useful for voice assistant systems.")

print()
print("SEMANTIC REPRESENTATION")

print("BOOK_FLIGHT(")
print("    DESTINATION = DELHI,")
print("    SEAT = WINDOW")
print(")")

print()
print("TOP-DOWN VS EARLEY PARSING")

print()
print("TOP-DOWN PARSING")
print("Starting point : Start symbol")
print("Ambiguity      : Backtracking may be required")
print("Partial input  : Limited handling")
print("Efficiency     : Can decrease with ambiguity")
print("Real-time use  : Less suitable")

print()
print("EARLEY PARSING")
print("Starting point : Chart-based parsing")
print("Ambiguity      : Handles multiple parses")
print("Partial input  : Better support")
print("Efficiency     : Avoids repeated states")
print("Real-time use  : More suitable")

print()
print("FINAL RESULT")
print("Intent          :", intent)
print("Destination     :", destination)
print("Seat Preference :", seat_preference)
print("Earley parsing is preferred for real-time voice assistant systems.")
