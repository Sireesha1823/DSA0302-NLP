import nltk

from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'sees' | 'likes'
""")

parser = ChartParser(grammar)

sentence = input("Enter a sentence: ").lower().split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()