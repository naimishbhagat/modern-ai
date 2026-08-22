from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash", 
    messages=[
        {"role": "system", "content":"You are an expert in Maths and only answer maths related questions"},
        {"role":"user","content":"Hey, Can you code a python program that can print hello?"}
    ]
)
print(response.choices[0].message.content)