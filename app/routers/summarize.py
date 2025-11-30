from fastapi import APIRouter
from pydantic import BaseModel
from app.core.model_loader import get_summarizer

router = APIRouter()

class SummarizeRequest(BaseModel):
    text: str

@router.post("/summarize")
def summarize(req: SummarizeRequest):
    summarizer = get_summarizer()
    result = summarizer(
        req.text,
        max_length=80,
        min_length=20,
        do_sample=False
    )
    return {"summary": result[0]["summary_text"]}
