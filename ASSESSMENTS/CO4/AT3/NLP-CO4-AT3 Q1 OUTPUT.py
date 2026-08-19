Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
======== RESTART: C:/Users/Sireesha/OneDrive/Documents/NLP-CO4-AT3 Q1.py =======
Original Sentence:
The boy eats the apple

----- CFG TREE -----
S
|-- NP
|   |-- Det -> The
|   |-- N   -> boy
|
|-- VP
    |-- V  -> eats
    |
    |-- NP
        |-- Det -> the
        |-- N   -> apple

----- DEPENDENCY PARSING -----
eats -> subject -> boy
eats -> object -> apple
boy -> determiner -> The
apple -> determiner -> the

----- RESULT -----
CFG represents the sentence using a tree structure.
Dependency parsing represents relationships between words.
