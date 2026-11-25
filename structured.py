from dotenv import load_dotenv
load_dotenv()

import json
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input="""Extract the data and return ONLY valid JSON, no extra text,
no markdown fences. Schema:
{"name": string, "date": "YYYY-MM-DD", "amount": number}

Text: "Rahul Sharma paid 2500 rupees on 5th March 2026 for the subscription." """
)

raw = interaction.output_text
print(raw)

clean = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
data = json.loads(clean)

print(data["name"], data["amount"],data["date"])