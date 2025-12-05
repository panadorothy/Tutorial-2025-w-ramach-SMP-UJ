import nltk

# Download only what is needed for sentiment analysis
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

# ---------------------------
# Sentiment Analysis Function
# ---------------------------
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    return scores

# ---------------------------
# Example
# ---------------------------
if __name__ == "__main__":
    sample_text = "text"
    sentiment = analyze_sentiment(sample_text)

    print("Text:", sample_text)
    print("Sentiment Scores:", sentiment)

# ---------------------------
# Komentarz pozytywny:
# Great idea! Thanks for sharing! What a great way to show off those awesome stamps!!
# ---------------------------
# ---------------------------
# Komentarz negatywny:
# 
# ---------------------------
# Komentarz mieszany:
# 
# ---------------------------
