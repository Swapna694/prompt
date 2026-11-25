from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    system_instruction="You are a agriculturist.",
    input="what is medicine for cough"
)

print(interaction.output_text)