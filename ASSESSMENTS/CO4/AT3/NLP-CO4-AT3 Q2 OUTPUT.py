Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

======== RESTART: C:/Users/Sireesha/OneDrive/Documents/NLP-CO4-AT3 Q2.py =======
Original Sentence:
John reads the book

----- TOP-DOWN PARSING -----
Start Symbol: S
S
|-- NP
|   |-- John
|
|-- VP
    |-- V -> reads
    |
    |-- NP
        |-- Det -> the
        |-- N -> book

----- EARLEY PARSING -----
Step 1: Prediction
S -> NP VP

Step 2: Scanning
NP -> John

Step 3: Prediction
VP -> V NP

Step 4: Scanning
V -> reads

Step 5: Prediction
NP -> Det N

Step 6: Scanning
Det -> the
N -> book

----- EARLEY PARSE TREE -----
S
|-- NP
|   |-- John
|
|-- VP
    |-- V -> reads
    |
    |-- NP
        |-- Det -> the
        |-- N -> book

----- RESULT -----
Top-Down parsing starts from the start symbol.
Earley parsing uses prediction, scanning and completion.
Earley parsing is suitable for incomplete and ambiguous input.
