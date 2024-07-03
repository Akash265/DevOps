# Import necessary libraries
from textblob import TextBlob
import nltk
from transformers import pipeline
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

# Initialize NLTK VADER sentiment intensity analyzer
nltk_analyzer = SentimentIntensityAnalyzer()

# Initialize Hugging Face pipeline for zero-shot classification
hf_classifier = pipeline(
    task="zero-shot-classification", model="facebook/bart-large-mnli"
)


def analyze_sentiment_textblob(text):
    blob = TextBlob(text)
    polarity, _ = blob.sentiment.polarity, blob.sentiment.subjectivity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment


def analyze_sentiment_nltk(text):
    scores = nltk_analyzer.polarity_scores(text)
    compound_score = scores["compound"]
    if compound_score >= 0.05:
        sentiment = "positive"
    elif compound_score <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment


def analyze_sentiment_hf(text):
    result = hf_classifier(
        text, candidate_labels=["positive", "negative", "neutral"], multi_label=True
    )
    return max(
        result["labels"], key=lambda x: result["scores"][result["labels"].index(x)]
    )


def analyze_sentiment(text):
    results = {
        "TextBlob": analyze_sentiment_textblob(text),
        "NLTK": analyze_sentiment_nltk(text),
        "HuggingFace": analyze_sentiment_hf(text),
    }
    return results
