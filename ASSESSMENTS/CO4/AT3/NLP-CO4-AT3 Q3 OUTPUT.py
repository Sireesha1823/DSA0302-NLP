Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

======== RESTART: C:/Users/Sireesha/OneDrive/Documents/NLP-CO4-AT3 Q3.py =======
Original Sentence:
She saw the man with a telescope

----- CFG PARSING -----
CFG generates possible sentence structures.

Interpretation 1:
She [saw the man] [with a telescope]
Meaning: She used a telescope to see the man.

Interpretation 2:
She [saw [the man with a telescope]]
Meaning: The man had a telescope.

----- PCFG PARSING -----
PCFG assigns probabilities to different
possible parse structures.

Interpretation 1 Probability: 0.7
Interpretation 2 Probability: 0.3

PCFG selects Interpretation 1

----- NEURAL PARSING -----
Neural parsing uses learned language patterns
and contextual information.

Input:
She saw the man with a telescope

Neural Parser Analysis:
The parser considers the context of the sentence.

Selected Interpretation:
She used a telescope to see the man.

----- COMPARISON -----
CFG:
Generates possible grammatical structures.

PCFG:
Assigns probabilities to possible structures.

Neural Parsing:
Uses learned contextual information to resolve ambiguity.

----- RESULT -----
CFG can identify multiple interpretations.
PCFG can rank interpretations using probabilities.
Neural parsing can use contextual information
to select the most suitable interpretation.
