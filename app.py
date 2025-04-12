from flask import Flask, request, jsonify
from utils.pdf_converter import convert_pdf_to_images
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_pdf():
    file = request.files["pdf"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    images = convert_pdf_to_images(path)
    return jsonify({"converted_images": images})

@app.route("/")
def home():
    return "Visiting Card OCR is running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)