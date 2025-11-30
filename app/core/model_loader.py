from transformers import pipeline
from functools import lru_cache

@lru_cache
def get_summarizer():
    """
    Loads the summarization model once and caches it for reuse.
    """
    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )
    return summarizer
