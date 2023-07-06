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


def skillRecommendation(jobTitle, skills):
    prompt = f"Job Title: {jobTitle}\nSkills: {skills}\nMissing Skills:"
    print(prompt)

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
        "Authorization": f"Bearer {api_key}",
    }

    response = requests.post(url, json=payload, headers=headers)

    response_text = response.text
    response_json = json.loads(response_text)

    completion = response_json["completions"][0]
    output_text = completion["data"]["text"]

    print(output_text)
    return output_text


# test case
# jobTitle = "Data Science Intern"
# skills = "Python, PowerBI, SQL"
# skillRecommendation(jobTitle, skills)
