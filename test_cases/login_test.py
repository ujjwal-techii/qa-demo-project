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

print ("Testing haseeb")

print("Testing haseeb")
print("Testing haseeb")
print("Testing haseeb")
print("Testing haseeb")
print("Testing haseeb")
print("Testing haseeb")


print("Testing 1")
print("Testing 2")
print("Testing 3")
print("Testing 4")
print("Testing 5")
print("Testing 6")


def getusername():
    return "ujjwal_Thakur"


getusername()