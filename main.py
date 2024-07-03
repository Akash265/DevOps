from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from mylib.logic import analyze_sentiment

app = FastAPI()

class TextRequest(BaseModel):
    text: str
@app.get("/")
def root():
    return {"message":"Sentiment Analysis"}

@app.post("/analyze_sentiment/")
def analyze_sentiment_endpoint(request: TextRequest):
    """
    Endpoint to analyze sentiment of the given text.
    """
    sentiments = analyze_sentiment(request.text)
    return sentiments

# Example usage for testing
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
