from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment(news):
    # Initializing the sentiment intensity analyzer
    sia = SentimentIntensityAnalyzer()
    # Calculating the polarity score for the news headline
    sentiment = sia.polarity_scores(news)
    # Returning the polarity score
    return sentiment