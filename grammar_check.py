import ai21
import os
import warnings

from dotenv import load_dotenv

# Load environment variables from .env.local file
load_dotenv(".env.local")

# Access the API key
api_key = os.getenv("API_KEY")

ai21.api_key = api_key


def grammarCheck(text):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            lines = text.split(
                "\n"
            )  # Split the text into lines based on new line characters
            chunk_lines = []
            chunks = []
            for line in lines:
                chunk_lines.append(line)
                if len(" ".join(chunk_lines)) > 500:
                    chunks.append("\n".join(chunk_lines))
                    chunk_lines = []
            if chunk_lines:
                chunks.append("\n".join(chunk_lines))

            corrections = []
            for chunk in chunks:
                response = ai21.GEC.execute(text=chunk)
                corrections.extend(response.corrections)
        return corrections
    except Exception as e:
        # Log the error message
        print("Error occurred during grammar checking:", str(e))
        return []


def getLineNo(text, errors):
    lines = text.split("\n")
    errorLines = []

    for error in errors:
        size = 0
        for i, line in enumerate(lines):
            if error["startIndex"] < (size + len(line)):
                errorLines.append(i + 1)
                break
            size += len(line) + 1
    return errorLines
