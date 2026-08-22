#Few shot prompting: The model is provided with a few examples before asking it to generate a response.

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key="AQ.Ab8RN6JYO8XUD7pYyJfa_AxB7FT6FBqPYGFoi-_niT76tOsM4Q",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Few shot prompt: Directly giving the instruction to the model and few examples to the model
SYSTEM_PROMPT = """
You should only answer coding related questions. 
Do not answer anything else.Your name is Alexa. 
If user asks something other than coding, just say sorry.

Rule:
- Strictly follow the outpit in JSON format

Output Format:
{{
    "code": "string" or "None",
    "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: Sorry, I can only help with coding related questions.

Q: Hey, Write a code in python for adding two numbers.
A: def add(a,b):
        return a+b
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash", 
    messages=[
        {"role": "system", "content":SYSTEM_PROMPT},
        {"role":"user","content":"Hey,write a code to add n numbers in js?"}
    ]
)
print(response.choices[0].message.content)