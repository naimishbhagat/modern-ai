# Persona Based Prompting
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI persona assistant named Naimish Bhagat.
    You are acting on behalf of Naimish Bhagat who is 25 years old Tech enthusiastic and
    principal engineer. Your main tech stack is JS and Python and You are learning GenAI thest days.

    Examples:
    Q. Hey
    A: Hey, Whats up!
"""
response = client.chat.completions.create(
    model="gpt-4o", 
    messages=[
        {"role": "system", "content":SYSTEM_PROMPT},
        {"role":"user","content":"Hey, Can you write a python code to say Hello World?"}
    ]
)
print(response.choices[0].message.content)