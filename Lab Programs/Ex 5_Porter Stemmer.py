from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running", "playing", "studies", "happiness", "cats"]

print("Word\t\tStem")

for word in words:
    print(word, "\t", ps.stem(word))