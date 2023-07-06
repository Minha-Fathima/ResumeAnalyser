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
            chunks = []
            current_chunk = ""
            for line in lines:
                if len(current_chunk) + len(line) + 1 > 500:
                    chunks.append(current_chunk)
                    current_chunk = line
                else:
                    current_chunk += "\n" + line
            if current_chunk:
                chunks.append(current_chunk)

            print("Total text length:", len(text))
            for i, chunk in enumerate(chunks, start=1):
                print(f"Chunk {i} length:", len(chunk))

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


# test case:
# text = "Joe Burg\nDubai, UAE \nJb23@hw.ac.uk \nObjective: \nHighy motivated and detail-oriented data science enthusiast seeking a challenging internship position in a dynamic organization apply and enhance my skills in data analysis, machine learning, and statistical modeling. \nDedicated to leveraging data-driven insights to drive informed business decisions. \nEducation: \nBachelor of Science in Data Science [Year - Year] \n[University Name], [City, State] \nRelevant coursework: \nMachine Learning, Statistical Analyss, Data Visualization, Python Programming, Database Management, Data Mining, Probability and Statistics. \nSkills:\n- Python\n- PowerBI\n- SQL\nProjects: \n1. Predictive Analytics for Customer Churn [University Project] \n- Utilized machine learning techniques to develop a predictive model for customer churn use a real wprld dataset. \n- Conducted exploratory data analysis to identify key features and patterns contributing to customer churn. \n- Implemented and fine-tuned various classification algoithms, including logistic regression and random forests, to predict customer churn. \n- Achieved an accuracy rate of 85% and presented the findings to the project team\n2. Sentiment Analysis of Social Media Data [Personal Project] \n- Gathered a large dataset from Twitter using the Twitter API and Python. \n- Preprocessed the data by removing noise, tokenizing, and normalizing the text. \n- Applied natural language processing techniques to perform sentiment analysis and classify tweets as positive, negative, or neutral. \n- Visualized the sentiment distribution using matplotlib and presented the results in a comprehensive report. Work Experience: Data Analyst Intern [Company Name], [City, State] [Month, Year - Month, Year]\n- Assisted in data collection, cleaning, and preprocessing tasks. \n- Conducted data analysis to identify patterns, trends, and insights. \n- Developed interactive dashboards using Tableau to visualize and present data findings to stakeholders. \n- Collaborated with the team to develop machine learning models for predictive analytics. \n- Assisted in the preparation of reports and presentations for management. \nCertifications: \n- Data Science Certification, [Certification Authority], [Year]\n- Machine Learning Fundamentals, [Certification Authority], [Year] \n- SQL Fundamentals, [Certification Authority], [Year] Professional Affiliations: \n- Member, [Data Science Society], [Year - Present] \n- Member, [Machine Learning Group], [Year - Present]"
# print(grammarCheck(text))
