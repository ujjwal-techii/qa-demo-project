# Haseeb Code
# Date 23 July


import requests

# Base URL of the API
BASE_URL = "https://example.com/api"  # Replace with your actual base URL

# Dummy credentials
payload = {
    "email": "user@example.com",
    "password": "securepassword123"
}

# Headers (if required)
headers = {
    "Content-Type": "application/json"
}

# Make the POST request to /login
response = requests.post(f"{BASE_URL}/login", json=payload, headers=headers)

# Output results
print(f"Status Code: {response.status_code}")
print("Response Body:", response.json())

# Example: check if login was successful
if response.status_code == 200 and "token" in response.json():
    print("✅ Login successful!")
    print("Token:", response.json()['token'])
else:
    print("❌ Login failed!")
