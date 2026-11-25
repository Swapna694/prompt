from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input="""Summarize the text below for a non-technical executive.
Rules:
- Exactly 2 bullet points
- Each under 15 words
- Focus on business impact, not technology

<text>
Our company launched a new mobile app that cut customer onboarding time
from 10 days to 2 days. The app uses a new identity-verification service
built on machine learning. Early users report higher satisfaction.
</text>"""
)

print(interaction.output_text)