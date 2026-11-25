from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input="""A person has 25 lakh rupees. He puts 20 lakh in a fixed deposit at 7.5%
    interest per year and the remaining amount in a savings account at 1.5%
    interest per year. Interest on both is compounded annually
    what is amount after 10 years?
    Think step by step inside <reasoning> tags,
    then give the final answer in lakh rupees inside <answer> tags."""
)

print(interaction.output_text)