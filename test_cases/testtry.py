from google import genai

client = genai.Client(api_key="AIzaSyDid1_lCayYEAHXgzYXWqNofTFUirvGDZY")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Hello how are u ?"
)
print(response.text)

from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)