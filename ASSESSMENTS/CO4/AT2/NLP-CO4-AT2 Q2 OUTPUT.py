Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
======== RESTART: C:/Users/Sireesha/OneDrive/Documents/NLP-CO4-AT2 Q2.py =======
VOICE ASSISTANT - FLIGHT BOOKING

INPUT COMMAND:
Book a flight to Delhi with a window seat

TOKENIZATION
['book', 'a', 'flight', 'to', 'delhi', 'with', 'a', 'window', 'seat']

IMPORTANT INFORMATION
Intent          : BOOK FLIGHT
Destination     : DELHI
Seat Preference : WINDOW

AMBIGUITY ANALYSIS
The phrase 'with a window seat' can create a prepositional phrase attachment ambiguity.

Possible Interpretation 1:
Book a flight to Delhi and give the passenger a window seat.

Possible Interpretation 2:
The phrase 'with a window seat' may be attached to the flight noun phrase.

POSSIBLE PARSE STRUCTURE
S
|-- VP
    |-- V -> Book
    |-- NP -> a flight
    |-- PP -> to Delhi
    |-- PP -> with a window seat

TOP-DOWN PARSING
S
↓
VP
↓
V + NP
↓
Book + a flight
↓
to Delhi + with a window seat

LIMITATIONS OF TOP-DOWN PARSING
1. It may require backtracking.
2. Ambiguous input can create multiple choices.
3. It may repeat parsing operations.
4. It can be inefficient for complex input.
5. It has limited support for incomplete commands.
6. Backtracking can increase response time.

EARLEY PARSING
PREDICT
Predict possible grammar rules.
SCAN
Match the next word with the grammar.
COMPLETE
Complete the recognized grammatical structure.

EARLEY PARSING ADVANTAGES
1. Handles ambiguous sentences.
2. Handles complex CFG grammars.
3. Stores intermediate parsing states.
4. Reduces repeated computation.
5. Handles partial input.
6. Suitable for real-time applications.
7. Useful for voice assistant systems.

SEMANTIC REPRESENTATION
BOOK_FLIGHT(
    DESTINATION = DELHI,
    SEAT = WINDOW
)

TOP-DOWN VS EARLEY PARSING

TOP-DOWN PARSING
Starting point : Start symbol
Ambiguity      : Backtracking may be required
Partial input  : Limited handling
Efficiency     : Can decrease with ambiguity
Real-time use  : Less suitable

EARLEY PARSING
Starting point : Chart-based parsing
Ambiguity      : Handles multiple parses
Partial input  : Better support
Efficiency     : Avoids repeated states
Real-time use  : More suitable

FINAL RESULT
Intent          : BOOK FLIGHT
Destination     : DELHI
Seat Preference : WINDOW
Earley parsing is preferred for real-time voice assistant systems.
