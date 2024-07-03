from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Sentiment Analysis"}

def test_analyze_sentiment_positive():
    response = client.post("/analyze_sentiment/", json={"text": "Very good service offered by the team."})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["TextBlob"] == "positive"
    assert json_response["NLTK"] == "positive"
    assert json_response["HuggingFace"] == "positive"

def test_analyze_sentiment_negative():
    response = client.post("/analyze_sentiment/", json={"text": "The service was terrible and slow."})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["TextBlob"] == "negative"
    assert json_response["NLTK"] == "negative"
    assert json_response["HuggingFace"] == "negative"