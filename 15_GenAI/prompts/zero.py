#Zero shot prompting: The model is given a direct question or task without prior examples.

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero shot prompt: Directly giving the instruction to the model
SYSTEM_PROMPT ="You should only answer coding related questions. Do not answer anything else.Your name is Alexa. If user asks something other than coding, just say sorry."

response = client.chat.completions.create(
    model="gemini-2.5-flash", 
    messages=[
        {"role": "system", "content":SYSTEM_PROMPT},
        {"role":"user","content":"Hey, Can you write a python code to say Hello World?"}
    ]
)
print(response.choices[0].message.content)