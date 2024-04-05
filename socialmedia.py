import nltk
from nltk.corpus import movie_reviews
import random

# Download the dataset and other resources
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')

# Load the dataset
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)







