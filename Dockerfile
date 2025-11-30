# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app/app


# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirement file
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Download NLTK datasets
RUN python3 -m nltk.downloader stopwords punkt -d /usr/local/nltk_data
ENV NLTK_DATA=/usr/local/nltk_data
# Copy the full app
COPY app/ /app/app

ENV PYTHONPATH=/app

# Expose port 8000
EXPOSE 8000

# Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

