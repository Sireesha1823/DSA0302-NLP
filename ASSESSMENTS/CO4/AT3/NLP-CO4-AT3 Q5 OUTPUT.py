Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
======== RESTART: C:/Users/Sireesha/OneDrive/Documents/NLP-CO4-AT3 Q5.py =======
Original Sentence:
The boy eats an apple

===== TRANSITION-BASED PARSING =====
Initial Stack: []
Initial Buffer: ['The', 'boy', 'eats', 'an', 'apple']

SHIFT -> The
Stack : ['The']
Buffer: ['boy', 'eats', 'an', 'apple']

SHIFT -> boy
Stack : ['The', 'boy']
Buffer: ['eats', 'an', 'apple']

SHIFT -> eats
Stack : ['The', 'boy', 'eats']
Buffer: ['an', 'apple']

SHIFT -> an
Stack : ['The', 'boy', 'eats', 'an']
Buffer: ['apple']

SHIFT -> apple
Stack : ['The', 'boy', 'eats', 'an', 'apple']
Buffer: []

Transition-Based Parsing Completed.

===== TRANSITION DEPENDENCIES =====
eats -> subject -> boy
eats -> object -> apple
boy -> determiner -> The
apple -> determiner -> an

===== GRAPH-BASED PARSING =====
Dependency Graph:

eats -- subject --> boy
eats -- object --> apple
boy -- determiner --> The
apple -- determiner --> an

===== GRAPH STRUCTURE =====
             eats
            /    \
      subject    object
        /          \
      boy          apple
      /             /
 determiner     determiner
    /               /
   The             an

===== COMPARISON =====
Transition-Based Parsing:
1. Makes decisions step by step.
2. Processes the sentence sequentially.
3. It is generally fast.
4. It is suitable for large datasets.

Graph-Based Parsing:
1. Represents dependencies as a graph.
2. Considers possible relationships.
3. Selects the best dependency structure.
4. Provides global structural analysis.

===== RESULT =====
Transition-based parsing is suitable
for large-scale applications because
it provides fast sequential processing.

Graph-based parsing considers the
overall dependency structure and
provides global analysis.
