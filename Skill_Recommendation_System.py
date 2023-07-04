import ai21
import os
import requests
import json

from dotenv import load_dotenv

# Load environment variables from .env.local file
load_dotenv(".env.local")

# Access the API key
api_key = os.getenv("API_KEY")

ai21.api_key = api_key

jobTitle = "Data Science Intern"
skills = "Python, PowerBI, SQL"
prompt = f"Job Title: {jobTitle}\nSkills: {skills}\nMissing Skills:"
print(prompt)
import requests

url = "https://api.ai21.com/studio/v1/j2-mid/Skill_Recommendation_System/complete"

payload = {
    "numResults": 3,
    "maxTokens": 50,
    "minTokens": 0,
    "temperature": 0.7,
    "topP": 1,
    "topKReturn": 0,
    "frequencyPenalty": {
        "scale": 1,
        "applyToWhitespaces": True,
        "applyToPunctuations": True,
        "applyToNumbers": True,
        "applyToStopwords": True,
        "applyToEmojis": True,
    },
    "presencePenalty": {
        "scale": 0,
        "applyToWhitespaces": True,
        "applyToPunctuations": True,
        "applyToNumbers": True,
        "applyToStopwords": True,
        "applyToEmojis": True,
    },
    "countPenalty": {
        "scale": 0,
        "applyToWhitespaces": True,
        "applyToPunctuations": True,
        "applyToNumbers": True,
        "applyToStopwords": True,
        "applyToEmojis": True,
    },
    "prompt": prompt,
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer yvvZtOdtLF5s6DWn7dFWiD3QGQNKRyCV",
}

response = requests.post(url, json=payload, headers=headers)

response_text = response.text
response_json = json.loads(response_text)

completion = response_json["completions"][0]
output_text = completion["data"]["text"]

print(output_text)

# print(response.text)


# url = "https://api.ai21.com/studio/v1/j1-grande/Skill_Recommendation_System/complete"

# payload = {
#     "numResults": 1,
#     "maxTokens": 16,
#     "minTokens": 0,
#     "temperature": 0.7,
#     "topP": 1,
#     "topKReturn": 0,
#     "frequencyPenalty": {
#         "scale": 1,
#         "applyToWhitespaces": True,
#         "applyToPunctuations": True,
#         "applyToNumbers": True,
#         "applyToStopwords": True,
#         "applyToEmojis": True,
#     },
#     "presencePenalty": {
#         "scale": 0,
#         "applyToWhitespaces": True,
#         "applyToPunctuations": True,
#         "applyToNumbers": True,
#         "applyToStopwords": True,
#         "applyToEmojis": True,
#     },
#     "countPenalty": {
#         "scale": 0,
#         "applyToWhitespaces": True,
#         "applyToPunctuations": True,
#         "applyToNumbers": True,
#         "applyToStopwords": True,
#         "applyToEmojis": True,
#     },
#     "prompt": "prompt",
# }
# headers = {
#     "accept": "application/json",
#     "content-type": "application/json",
#     "Authorization": "Bearer {api_key}",
# }

# response = requests.post(url, json=payload, headers=headers)


# r = requests.post(
#     "https://api.ai21.com/studio/v1/j2-grande/Skill_Recommendation_System/complete",
#     headers={"Authorization": "Bearer {api_key}"},
#     json={
#         "prompt": prompt,
#         "numResults": 1,
#         "maxTokens": 200,
#         "temperature": 0.7,
#         "topKReturn": 0,
#     },
# )

# print(r.text)


# ai21.api_key = api_key

# response = ai21.Completion.execute(
#     model="j2-light",
#     prompt="Classify the following news article into one of the following topics:\n1. World\n2. Sports\n3. Business\n4. Science and Technology\nTitle:\nAstronomers Observe Collision of Galaxies, Formation of Lightr\nSummary:\nAn international team of astronomers has obtained the clearest images yet of the merger of two distant clusters of galaxies, calling it one of the most powerful cosmic events ever witnessed.\nThe topic of this article is:",
#     numResults=1,
#     maxTokens=10,
#     temperature=0,
#     topKReturn=0,
#     topP=1,
#     countPenalty={
#         "scale": 0,
#         "applyToNumbers": False,
#         "applyToPunctuations": False,
#         "applyToStopwords": False,
#         "applyToWhitespaces": False,
#         "applyToEmojis": False,
#     },
#     frequencyPenalty={
#         "scale": 0,
#         "applyToNumbers": False,
#         "applyToPunctuations": False,
#         "applyToStopwords": False,
#         "applyToWhitespaces": False,
#         "applyToEmojis": False,
#     },
#     presencePenalty={
#         "scale": 0,
#         "applyToNumbers": False,
#         "applyToPunctuations": False,
#         "applyToStopwords": False,
#         "applyToWhitespaces": False,
#         "applyToEmojis": False,
#     },
#     stopSequences=["==="],
# )
# print(response.text)

# response = ai21.Completion.execute(
#     model="j2-grande",
#     custom_model="Skill_Recommendation_System",
#     prompt=prompt,
#     numResults=1,
#     maxTokens=200,
#     temperature=0.7,
#     topKReturn=0,
#     topP=1,
#     countPenalty={
#         "scale": 0,
#         "applyToNumbers": False,
#         "applyToPunctuations": False,
#         "applyToStopwords": False,
#         "applyToWhitespaces": False,
#         "applyToEmojis": False,
#     },
#     frequencyPenalty={
#         "scale": 0,
#         "applyToNumbers": False,
#         "applyToPunctuations": False,
#         "applyToStopwords": False,
#         "applyToWhitespaces": False,
#         "applyToEmojis": False,
#     },
#     presencePenalty={
#         "scale": 0,
#         "applyToNumbers": False,
#         "applyToPunctuations": False,
#         "applyToStopwords": False,
#         "applyToWhitespaces": False,
#         "applyToEmojis": False,
#     },
#     stopSequences=[],
# )
