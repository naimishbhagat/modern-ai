from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)