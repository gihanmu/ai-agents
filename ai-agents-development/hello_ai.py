from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))
question = input("What is your question? ")

response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[{"role": "user", "content": question}]
)

print(response.choices[0].message.content)