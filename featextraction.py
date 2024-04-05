from sklearn.feature_extraction.text import CountVectorizer

# Flatten all documents for the CountVectorizer and separate labels
all_words = [" ".join(words) for (words, category) in documents]
categories = [category for (words, category) in documents]

# Create the CountVectorizer and transform our text
vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
features = vectorizer.fit_transform(all_words).toarray()
