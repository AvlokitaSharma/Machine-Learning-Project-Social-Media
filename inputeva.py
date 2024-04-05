def predict_sentiment(text):
    """Predict sentiment of a given text."""
    processed = preprocess_words(nltk.word_tokenize(text))
    vectorized = vectorizer.transform([" ".join(processed)])
    prediction = classifier.predict(vectorized.toarray())
    return prediction[0]

# Example usage
text = "This movie was an excellent portrayal of character development and had stunning visuals."
print(f"Sentiment: {predict_sentiment(text)}")
