import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download resources (first time only)
nltk.download('wordnet')
nltk.download('omw-1.4')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["running", "playing", "studies", "better", "cars"]

print("Word\t\tStem\t\tLemma")

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"{word}\t\t{stem}\t\t{lemma}")