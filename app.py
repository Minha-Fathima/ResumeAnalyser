# from flask import render_template, request, Flask
# from pdf_to_text import pdfToText
# from grammar_check import grammarCheck, getLineNo

# app = Flask(__name__)
# app.debug = True


# # Set up the route for the home page
# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/", methods=["POST"])
# def upload_file():
#     file = request.files["file"]
#     if file and file.filename.endswith(".pdf"):
#         text = pdfToText(file)
#         grammar_errors = grammarCheck(text)
#         line = getLineNo(text, grammar_errors)
#         # print(grammar_errors)
#         # print(line)
#         return render_template(
#             "index.html", text=text, grammar_errors=grammar_errors, line=line
#         )
#     else:
#         return render_template("index.html")


# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000)

import os
import ai21
import PyPDF2
from dotenv import load_dotenv
from flask import Flask, render_template, request
import warnings

app = Flask(__name__)
app.debug = True

# Load environment variables from .env.local file
load_dotenv(".env.local")

# Access the API key
api_key = os.getenv("API_KEY")

# Set up the route for the home page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload_file():
    file = request.files["file"]
    if file and file.filename.endswith(".pdf"):
        text = pdfToText(file)
        grammar_errors = grammarCheck(text)
        line = getLineNo(text)
        return render_template(
            "index.html", text=text, grammar_errors=grammar_errors, line=line
        )
    else:
        return render_template("index.html")

def grammarCheck(text):
    ai21.api_key = api_key
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        chunk_size = 500  # Set the desired chunk size
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        corrections = []
        for chunk in chunks:
            response = ai21.GEC.execute(text=chunk)
            corrections.extend(response.corrections)
    return corrections

def getLineNo(text):
    lines = text.split("\n")
    return len(lines)

def pdfToText(file):
    text = ""
    reader = PyPDF2.PdfReader(file)

    for page in reader.pages:
        text += page.extract_text()
    return text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
