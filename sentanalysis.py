# Simple Sentiment Analysis Program in Python
# Step by step with explanations

# 1. Import the tools we need
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 2. Make some example sentences (our dataset)
positive_sentences = [
    "I love this product",
    "This is the best thing ever",
    "I am very happy with the service"
]

negative_sentences = [
    "I hate this product",
    "This is the worst thing ever",
    "I am very sad and disappointed"
]

# 3. Put all sentences together in one list
texts = positive_sentences + negative_sentences

# 4. Make labels for them
#    'positive' for first 3, 'negative' for last 3
labels = [
    "positive", "positive", "positive",
    "negative", "negative", "negative"
]

# 5. Change the text into numbers (Bag of Words)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# 6. Create the model (Naive Bayes)
model = MultinomialNB()

# 7. Train the model with our data
model.fit(X, labels)

# 8. Now test the model with new sentences
test_sentences = [
    "I really love this",   # should be positive
    "This is terrible",     # should be negative
    "I am happy",           # should be positive
    "I am angry and sad"    # should be negative
]

# 9. Convert test sentences into numbers
X_test = vectorizer.transform(test_sentences)

# 10. Predict their sentiment
predictions = model.predict(X_test)

# 11. Print the results
for sentence, sentiment in zip(test_sentences, predictions):
    print("Text:", sentence, " --> Sentiment:", sentiment)
