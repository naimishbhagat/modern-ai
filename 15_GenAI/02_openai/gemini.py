from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(
    api_key="AQ.Ab8RN6JYO8XUD7pYyJfa_AxB7FT6FBqPYGFoi-_niT76tOsM4Q",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)