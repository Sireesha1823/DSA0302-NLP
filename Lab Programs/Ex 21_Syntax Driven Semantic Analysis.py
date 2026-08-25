import re

# Function to extract noun phrases
def extract_noun_phrases(sentence):
    # Simple pattern for noun phrases
    pattern = r'\b(the|a|an)?\s*(\w+\s+){0,2}(boy|girl|student|teacher|book|dog|cat|car|school|computer|language)\b'

    matches = re.findall(pattern, sentence.lower())

    noun_phrases = []

    for match in matches:
        phrase = " ".join(match).strip()
        if phrase:
            noun_phrases.append(phrase)

    return noun_phrases


# Function to assign simple meanings
def get_meaning(noun_phrase):
    meanings = {
        "boy": "a male child",
        "girl": "a female child",
        "student": "a person who studies",
        "teacher": "a person who teaches",
        "book": "a written or printed work",
        "dog": "a domesticated animal",
        "cat": "a small domesticated animal",
        "car": "a vehicle used for transportation",
        "school": "an institution for education",
        "computer": "an electronic device used for processing information",
        "language": "a system used for communication"
    }

    words = noun_phrase.split()

    for word in words:
        if word in meanings:
            return meanings[word]

    return "Meaning not available"


# Input sentence
sentence = input("Enter a sentence: ")

# Extract noun phrases
noun_phrases = extract_noun_phrases(sentence)

print("\nNoun Phrases and Their Meanings")
print("--------------------------------")

if noun_phrases:
    for phrase in noun_phrases:
        print("Noun Phrase:", phrase)
        print("Meaning:", get_meaning(phrase))
        print()
else:
    print("No noun phrases found.")