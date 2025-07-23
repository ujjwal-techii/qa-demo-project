import json

import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# Sending GET request
response = requests.get(url)

# Checking response status
if response.status_code == 200:
    pretty_json =  json.dumps(response.json(), indent=4)
    print(pretty_json)  # Parse JSON response
else:
    print(f"Failed! Status Code: {response.status_code}")
