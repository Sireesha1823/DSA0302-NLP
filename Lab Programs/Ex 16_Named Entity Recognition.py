import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a sentence: ")

doc = nlp(text)

for entity in doc.ents:
    print(entity.text, "->", entity.label_)