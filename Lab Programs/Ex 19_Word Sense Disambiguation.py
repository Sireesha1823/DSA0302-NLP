import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('punkt_tab')

def lesk(sentence, word):
    # Tokenize the sentence
    context = set(word_tokenize(sentence.lower()))

    best_sense = None
    max_overlap = 0

    # Get all possible meanings of the word
    for sense in wordnet.synsets(word):

        # Create the meaning signature
        signature = set(
            word_tokenize(
                sense.definition().lower()
                + " "
                + " ".join(sense.examples()).lower()
            )
        )

        # Find common words
        overlap = len(context.intersection(signature))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense, max_overlap


# Get input
sentence = input("Enter a sentence: ")
word = input("Enter the ambiguous word: ")

# Apply Lesk algorithm
sense, score = lesk(sentence, word)

# Display result
if sense:
    print("\nWord:", word)
    print("Best Sense:", sense.name())
    print("Meaning:", sense.definition())
    print("Overlap Score:", score)
else:
    print("\nNo suitable meaning found.")