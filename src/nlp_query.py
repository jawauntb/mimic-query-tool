import openai
from dotenv import load_dotenv
import os
import pandas as pd

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load metadata
metadata = pd.read_csv('data/metadata.csv')

# Example query
user_query = "Find papers on the effectiveness of masks for COVID-19 prevention."

# Use GPT for translation
response = openai.Completion.create(
    engine="gpt-4o-mini",
    prompt=f"Retrieve abstracts related to: {user_query}",
    max_tokens=100
)

print(response.choices[0].text)
