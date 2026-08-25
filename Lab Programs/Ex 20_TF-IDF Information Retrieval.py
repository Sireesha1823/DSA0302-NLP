import math
import re
from collections import Counter

# Documents
documents = [
    "Natural language processing is a field of artificial intelligence",
    "Machine learning is used in artificial intelligence",
    "Natural language processing helps computers understand human language",
    "Information retrieval finds relevant documents from a collection"
]

# Query
query = input("Enter your search query: ")

# Function to tokenize text
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())


# Tokenize documents
tokenized_docs = [tokenize(doc) for doc in documents]

# Calculate IDF
all_words = set(word for doc in tokenized_docs for word in doc)

idf = {}

for word in all_words:
    document_count = sum(word in doc for doc in tokenized_docs)
    idf[word] = math.log(len(documents) / document_count)


# Calculate TF-IDF for each document
tfidf_documents = []

for doc in tokenized_docs:
    word_count = Counter(doc)
    total_words = len(doc)

    tfidf = {}

    for word in all_words:
        tf = word_count[word] / total_words
        tfidf[word] = tf * idf[word]

    tfidf_documents.append(tfidf)


# Calculate query TF-IDF
query_words = tokenize(query)
query_count = Counter(query_words)
query_tfidf = {}

for word in all_words:
    tf = query_count[word] / len(query_words)
    query_tfidf[word] = tf * idf[word]


# Calculate cosine similarity
def cosine_similarity(vector1, vector2):
    dot_product = sum(vector1[word] * vector2[word] for word in all_words)

    magnitude1 = math.sqrt(
        sum(vector1[word] ** 2 for word in all_words)
    )

    magnitude2 = math.sqrt(
        sum(vector2[word] ** 2 for word in all_words)
    )

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product / (magnitude1 * magnitude2)


# Rank documents
scores = []

for i, doc_vector in enumerate(tfidf_documents):
    score = cosine_similarity(query_tfidf, doc_vector)
    scores.append((i, score))


scores.sort(key=lambda x: x[1], reverse=True)


# Display results
print("\nSearch Results:")
print("----------------------------")

for rank, (index, score) in enumerate(scores, start=1):
    print("Rank:", rank)
    print("Document:", documents[index])
    print("TF-IDF Similarity:", round(score, 4))
    print()