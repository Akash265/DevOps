from mylib.logic import analyze_sentiment_textblob, analyze_sentiment_nltk, analyze_sentiment_hf, analyze_sentiment

def test_analyze_sentiment_textblob():
    assert analyze_sentiment_textblob("Very good service offered by the team.") == "positive"
    assert analyze_sentiment_textblob("The service was terrible and slow.") == "negative"

def test_analyze_sentiment_nltk():
    assert analyze_sentiment_nltk("Very good service offered by the team.") == "positive"
    assert analyze_sentiment_nltk("The service was terrible and slow.") == "negative"

def test_analyze_sentiment_hf():
    assert analyze_sentiment_hf("Very good service offered by the team.") == "positive"
    assert analyze_sentiment_hf("The service was terrible and slow.") == "negative"
  

def test_analyze_sentiment():
    text = "Very good service offered by the team."
    results = analyze_sentiment(text)
    assert results["TextBlob"] == "positive"
    assert results["NLTK"] == "positive"
    assert results["HuggingFace"] == "positive"

    text = "The service was terrible and slow."
    results = analyze_sentiment(text)
    assert results["TextBlob"] == "negative"
    assert results["NLTK"] == "negative"
    assert results["HuggingFace"] == "negative"
