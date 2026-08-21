Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
======== RESTART: C:/Users/Sireesha/OneDrive/Documents/NLP-CO5-AT1 Q3.py =======
SOURCE SENTENCE
The bank by the river flooded after the storm, but it was saved by quick action.

1. WORD SENSE DISAMBIGUATION
----------------------------
Possible meanings:
- Financial institution
- Riverbank
Selected meaning: Riverbank

Reason:
The words 'river' and 'flooded' support the riverbank meaning.

2. PREDICATE LOGIC
------------------
RiverBank(b)
River(r)
LocatedBy(b,r)
Storm(s)
Flood(b)
After(Flood(b),s)
QuickAction(q)
Saved(b,q)

3. DISCOURSE RELATION
---------------------
Contrast(
    Flood(b) AND After(Flood(b),s),
    Saved(b,q)
)

4. DISCOURSE TREE
-----------------
                 CONTRAST
                /        \
               /          \
        Clause 1          Clause 2
           |                 |
     Bank flooded       Bank saved
     after storm        by quick action

5. TARGET SENTENCE
------------------
The riverbank flooded after the storm, but quick action helped save it.

6. FINAL RESULT
---------------
Bank = Riverbank
Discourse relation = Contrast
All important entities and relations are preserved.
