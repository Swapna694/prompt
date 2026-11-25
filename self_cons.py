from dotenv import load_dotenv
load_dotenv()

import time
from collections import Counter
from google import genai

client = genai.Client()

question = """A train leaves at 2:15 PM and the trip takes 3 hours 50 minutes.
Then there is a 25 minute bus ride. At what time do I arrive?
Think step by step, then put the final answer on the last line as: ANSWER: HH:MM AM/PM"""

answers = []
for i in range(5):
    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=question
    )
    last_line = interaction.output_text.strip().splitlines()[-1]
    print(f"Run {i + 1}:", last_line)
    answers.append(last_line)
    time.sleep(1)

print("Majority:", Counter(answers).most_common(1)[0])