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
    sample_text = "For everyone with negativity, do you think these young people asked for a war . Britian has fought many wars we didnt vote or ask for and many lives were lost in the process . This isnt a joke or time to ridicule people who are suffering. I would hope and pray for safety if anything happened in the UK . We are lucky enough to never see bombs drop on our homes and experience such trauma . I wish you both all the best"
    sentiment = analyze_sentiment(sample_text)

    print("Text:", sample_text)
    print("Sentiment Scores:", sentiment)
