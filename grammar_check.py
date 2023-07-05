import ai21
import os
import warnings

from dotenv import load_dotenv
from pdf_to_text import pdfToText

# Load environment variables from .env.local file
load_dotenv(".env.local")

# Access the API key
api_key = os.getenv("API_KEY")

ai21.api_key = api_key

# response = ai21.GEC.execute(
#   text="jazzz is a great stile off music")
# print(response)


# def grammarCheck(texts):
#     response = ai21.GEC.execute(text=texts)
#     return response.corrections

def grammarCheck(text):
    ai21.api_key = api_key
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        chunk_size = 500  # Set the desired chunk size
        chunks = [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]
        corrections = []
        for chunk in chunks:
            response = ai21.GEC.execute(text=chunk)
            corrections.extend(response.corrections)
    return corrections


def getLineNo(text,errors):
    lines = text.split("\n")
    errorLines = []    

    for error in errors:
        size = 0
        for i, line in enumerate(lines):
            if error['startIndex'] < (size + len(line)):
                errorLines.append(i+1)
                break
            size += len(line) + 1
    return errorLines
