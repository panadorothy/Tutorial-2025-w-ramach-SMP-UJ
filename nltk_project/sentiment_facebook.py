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
    sample_text = "If i break into someone's house i go to jail. If an illegal immigrant breaks into our country they get taxpayers money."
    sentiment = analyze_sentiment(sample_text)

    print("Text:", sample_text)
    print("Sentiment Scores:", sentiment)

# ---------------------------
# Komentarz pozytywny:
# Great idea! Thanks for sharing! What a great way to show off those awesome stamps!!
# ---------------------------
# ---------------------------
# Komentarz negatywny:
# If i break into someone's house i go to jail. If an illegal immigrant breaks into our country they get taxpayers money.
# ---------------------------
# Komentarz mieszany:
# I love it, it's an absolute genius move. Ukraine is writing a masterclass in future warfare. Frankly, I have zero sympathy for the Russians.
# ---------------------------
