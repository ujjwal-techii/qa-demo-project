from google import genai

client = genai.Client(api_key="AIzaSyDid1_lCayYEAHXgzYXWqNofTFUirvGDZY")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Hello how are u ?"
)
print(response.text)