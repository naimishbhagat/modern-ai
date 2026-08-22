from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key="AQ.Ab8RN6JYO8XUD7pYyJfa_AxB7FT6FBqPYGFoi-_niT76tOsM4Q",
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