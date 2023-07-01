import ai21
import os

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


def grammarCheck(texts):
    response = ai21.GEC.execute(text=texts)
    return response.corrections


def getLineNo(text):
    lines = text.split("\n")
