from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input="""Convert the date to YYYY-MM-DD.

    Input: 5th March 2026
    Output: 2026-03-05

    Input: 18th November 2025
    Output:"""
)

print(interaction.output_text)