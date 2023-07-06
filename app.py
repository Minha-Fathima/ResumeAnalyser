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

# import os
# from dotenv import load_dotenv
# from flask import Flask, render_template, request
# from pdf_to_text import pdfToText
# from grammar_check import grammarCheck, getLineNo

# app = Flask(__name__)
# app.debug = True

# # Load environment variables from .env.local file
# load_dotenv(".env.local")

# # Access the API key
# api_key = os.getenv("API_KEY")

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
#         return render_template(
#             "index.html", text=text, grammar_errors=grammar_errors, line=line
#         )
#     else:
#         return render_template("index.html")

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000)


import logging
from flask import render_template, request, Flask
from pdf_to_text import pdfToText
from grammar_check import grammarCheck, getLineNo
from extraction import Job_Title_Extraction, Skills_Extraction
from skill_recommendation import skillRecommendation
from certification_recommendation import certificateRecommendation

app = Flask(__name__)
# app.debug = True
app.logger.setLevel(logging.DEBUG)


# Set up the route for the home page
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload_file():
    file = request.files["file"]
    if file and file.filename.endswith(".pdf"):
        text = pdfToText(file)

        # grammer check
        grammar_errors = grammarCheck(text)
        line = getLineNo(text, grammar_errors)

        # skill recommendation
        job = Job_Title_Extraction(text)
        skill = Skills_Extraction(text)
        skillRec = skillRecommendation(job, skill)
        print(skillRec)
        skillRec = skillRec.split(",")
        print(skillRec)

        # certification recommendation
        certificateRec = certificateRecommendation(job)
        certificateRec = certificateRec.split(",")
        print(certificateRec)

        return render_template(
            "index.html",
            text=text,
            grammar_errors=grammar_errors,
            line=line,
            certificateRec=certificateRec,
            skillRec=skillRec,
        )
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

