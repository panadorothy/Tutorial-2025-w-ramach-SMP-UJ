import nltk

# Download all required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('snowball_data')

from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet


# ---------------------------
# Helper function for lemmatization
# ---------------------------
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN


# ---------------------------
# Example text
# ---------------------------
text = "Barack Obama was born in Hawaii, and he was the President of the United States. NLTK is a great package for working with natural language data."


# ---------------------------
# 1. Tokenization
# ---------------------------
tokens = word_tokenize(text)
print("Tokens:")
print(tokens)
print()


# ---------------------------
# 2. POS tagging
# ---------------------------
pos_tags = pos_tag(tokens)
print("POS Tags:")
print(pos_tags)
print()


# ---------------------------
# 3. Named Entity Recognition
# ---------------------------
ner_tree = ne_chunk(pos_tags)
print("Named Entities:")
print(ner_tree)
print()


# ---------------------------
# 4. Sentiment Analysis
# ---------------------------
analyzer = SentimentIntensityAnalyzer()
sentiment_scores = analyzer.polarity_scores(text)
print("Sentiment Scores:")
print(sentiment_scores)
print()


# ---------------------------
# 5. Stemming
# ---------------------------
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]
print("Stemmed Words:")
print(stemmed_words)
print()


# ---------------------------
# 6. Lemmatization
# ---------------------------
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]

print("Lemmatized Words:")
print(lemmatized_words)
print()
