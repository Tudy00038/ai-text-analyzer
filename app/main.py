from fastapi import FastAPI
from app.routers.summarize import router as summarize_router
from app.routers.keywords import router as keywords_router
from app.routers.sentiment import router as sentiment_router
app = FastAPI()
app.include_router(summarize_router)
app.include_router(keywords_router)
app.include_router(sentiment_router)
@app.get("/")
def root():
    return {"message": "AI Text Analyzer API is running!"}
