import json
import nltk
from fastapi import FastAPI
from utils import SentimentPredictor


app = FastAPI()
nltk.download('wordnet')

MODEL_PATH = "./sentiment_classifier.joblib"
LABELS = {0: "negative",1: "positive"}
predictor = SentimentPredictor(MODEL_PATH, LABELS)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/classify")
def classify_review(user_input: str) -> str:
    sentiment = predictor.run(
        user_input
    )
    print(f"Output Sentiment is  {sentiment}")
    
    return json.dumps({"sentiment" : sentiment})
    