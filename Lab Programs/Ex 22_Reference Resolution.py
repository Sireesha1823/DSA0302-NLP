import re

# Pronouns and their possible types
pronouns = {
    "he": "male person",
    "him": "male person",
    "his": "male person",
    "she": "female person",
    "her": "female person",
    "hers": "female person",
    "they": "person or group",
    "them": "person or group",
    "their": "person or group",
    "it": "object or thing"
}

# Function to find nouns in a sentence
def find_nouns(sentence):
    words = re.findall(r'\b[A-Za-z]+\b', sentence)

    common_nouns = {
        "student", "teacher", "boy", "girl", "man", "woman",
        "doctor", "engineer", "dog", "cat", "book", "car",
        "computer", "school", "college", "phone"
    }

    nouns = []

    for word in words:
        if word.lower() in common_nouns:
            nouns.append(word)

    return nouns


# Input text
text = input("Enter a text: ")

# Split text into sentences
sentences = re.split(r'[.!?]', text)

# Store recent nouns
previous_nouns = []

print("\nReference Resolution")
print("----------------------------")

for sentence in sentences:

    if not sentence.strip():
        continue

    nouns = find_nouns(sentence)

    # Find pronouns
    words = re.findall(r'\b[A-Za-z]+\b', sentence.lower())

    for word in words:
        if word in pronouns:

            if previous_nouns:
                reference = previous_nouns[-1]

                print("Pronoun:", word)
                print("Refers to:", reference)
                print()

            else:
                print("Pronoun:", word)
                print("Reference: Not found")
                print()

    # Update previous nouns
    previous_nouns.extend(nouns)