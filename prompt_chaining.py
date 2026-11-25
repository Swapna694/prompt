from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client()

email = "I ordered a laptop last week (order #4821). It arrived with a cracked screen. I want my money back."

# Step 1: classify
step1 = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input=f"Classify this email as REFUND, EXCHANGE, or OTHER. Return only the label.\n\n{email}"
)
print("STEP 1:", step1.output_text)

# Step 2: extract details
step2 = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input=f"Extract order_id and problem as JSON only.\n\n{email}"
)
print("STEP 2:", step2.output_text)

# Step 3: write a reply using the previous outputs
step3 = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input=f"""Write a polite support reply under 60 words.
Intent: {step1.output_text}
Details: {step2.output_text}"""
)
print("STEP 3:", step3.output_text)