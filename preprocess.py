from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_words(words):
    """Preprocess words: remove stopwords, punctuation, and apply lemmatization."""
    cleaned_words = [lemmatizer.lemmatize(word.lower()) for word in words if word.lower() not in stop_words and word not in string.punctuation]
    return cleaned_words

# Preprocess all documents
documents = [(preprocess_words(text), category) for (text, category) in documents]
