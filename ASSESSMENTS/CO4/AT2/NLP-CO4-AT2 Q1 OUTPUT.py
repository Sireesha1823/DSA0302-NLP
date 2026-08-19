Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

======== RESTART: C:/Users/Sireesha/OneDrive/Documents/NLP-CO4-AT2 Q1.py =======
========== BANKING CHATBOT ==========

Input:
Show me the transactions with the card from last month

========== AMBIGUITY ANALYSIS ==========
The sentence contains structural ambiguity.

Interpretation 1:
Show the transactions that were made using the card
and that occurred during last month.

Interpretation 2:
The phrase 'from last month' may be attached
to a different part of the sentence.

========== CFG REPRESENTATION ==========
S -> VP
VP -> V NP
NP -> DET NOUN PP PP
PP -> PREP NP
NP -> DET NOUN

Grammar interpretation:
S
|-- VP
    |-- V -> show
    |-- NP -> the transactions
        |-- PP -> with the card
        |-- PP -> from last month

========== SEMANTIC REPRESENTATION ==========
Intent      : SHOW_TRANSACTIONS
Object      : TRANSACTIONS
Instrument  : CARD
Time        : LAST_MONTH

========== PCFG ==========
Example probabilistic grammar rules:
NP -> DET NOUN PP PP     Probability = 0.60
NP -> DET NOUN           Probability = 0.40
PP -> PREP NP            Probability = 1.00

PCFG selects the most probable interpretation
when multiple parse structures are possible.

========== FEATURE STRUCTURE ==========
Subject/Object Features:
Number : Plural
Person : Third
Category : Noun

========== FINAL RESULT ==========
The chatbot interprets the query as:
SHOW the TRANSACTIONS
made using the CARD
during LAST MONTH.

Improved approach:
CFG + PCFG + Feature Structures + Earley Parsing
