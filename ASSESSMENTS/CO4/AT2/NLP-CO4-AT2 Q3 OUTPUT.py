Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
======== RESTART: C:/Users/Sireesha/OneDrive/Documents/NLP-CO4-AT2 Q3.py =======
HEALTHCARE REPORT NLP

INPUT SENTENCE:
The doctor who reviewed the patient last week recommends starting medication and scheduling a follow-up visit in Chennai.

1. TOKENIZATION
['the', 'doctor', 'who', 'reviewed', 'the', 'patient', 'last', 'week', 'recommends', 'starting', 'medication', 'and', 'scheduling', 'a', 'follow-up', 'visit', 'in', 'chennai']

2. MEDICAL ENTITIES
doctor -> Medical Professional
patient -> Patient
medication -> Treatment
follow-up visit -> Medical Action
Chennai -> Location
last week -> Time

3. CFG SYNTACTIC STRUCTURE
S
|-- NP
    |-- The doctor
    |-- Relative Clause
        |-- who reviewed the patient last week
|-- VP
    |-- recommends
    |-- starting medication
    |-- scheduling a follow-up visit in Chennai

4. FEATURE STRUCTURE
Doctor:
Category : Noun
Number   : Singular
Person   : Third

Recommends:
Category : Verb
Number   : Singular
Person   : Third

5. SUBJECT-VERB AGREEMENT
Subject-Verb Agreement is CORRECT

6. SUB-CATEGORIZATION
review
Subject : Doctor
Object  : Patient

recommend
Subject : Doctor
Object  : Medical Action

start
Object  : Medication

schedule
Object  : Follow-up Visit

7. PCFG AMBIGUITY RESOLUTION
Possible interpretations are generated.
PCFG assigns probabilities to the interpretations.
The most probable interpretation is selected.

Selected Interpretation:
Doctor recommends starting medication
and scheduling a follow-up visit in Chennai.

8. SEMANTIC RELATIONS
Doctor -- reviewed --> Patient
Doctor -- reviewed_time --> Last Week
Doctor -- recommends --> Starting Medication
Doctor -- recommends --> Scheduling Follow-up Visit
Follow-up Visit -- location --> Chennai

9. STRUCTURED OUTPUT
Medical Professional : Doctor
Patient             : Patient
Review Time         : Last Week
Treatment           : Medication
Action 1            : Start Medication
Action 2            : Schedule Follow-up Visit
Location            : Chennai
Diagnosis           : Not explicitly mentioned

10. NLP ARCHITECTURE
Input Medical Report
        ↓
Preprocessing
        ↓
Tokenization
        ↓
CFG Parsing
        ↓
PCFG Ambiguity Resolution
        ↓
Feature Structure Analysis
        ↓
Medical Entity Extraction
        ↓
Sub-Categorization
        ↓
Semantic Relation Extraction
        ↓
Structured Medical Output

11. FINAL RESULT
Medical information extracted successfully.
Treatment : Medication
Action    : Start Medication
Action    : Schedule Follow-up Visit
Location  : Chennai
