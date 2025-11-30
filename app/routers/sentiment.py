from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline
from functools import lru_cache

router = APIRouter()

@lru_cache
def get_sentiment_model():
    return pipeline("sentiment-analysis")

class SentimentRequest(BaseModel):
    text: str

@router.post("/sentiment")
def sentiment(req: SentimentRequest):
    model = get_sentiment_model()
    result = model(req.text)
    return {"label": result[0]["label"], "score": result[0]["score"]}
