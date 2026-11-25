from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input="Classify the sentiment as Positive, Negative, or Neutral. "
          "Return only the label.\n\nReview: 'my father bought me lot of chocolate.'"
)

print(interaction.output_text)