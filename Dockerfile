FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y poppler-utils tesseract-ocr
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]