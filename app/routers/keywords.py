from fastapi import APIRouter
from pydantic import BaseModel
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

router = APIRouter()

stop_words = set(stopwords.words("english"))
punct = set(string.punctuation)

class KeywordsRequest(BaseModel):
    text: str

@router.post("/keywords")
def get_keywords(req: KeywordsRequest):
    tokens = word_tokenize(req.text.lower())
    tokens = [t for t in tokens if t not in stop_words and t not in punct]

    freq = Counter(tokens)
    keywords = [w for w, _ in freq.most_common(5)]

    return {"keywords": keywords}
