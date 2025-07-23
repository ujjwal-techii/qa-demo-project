import json

import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# Sending GET request
response = requests.get(url)

# Checking response status
if response.status_code == 200:
    pretty_json =  json.dumps(response.json(), indent=4)
    pretty_json = json.dumps(response.json(), indent=4)
    pretty_json = json.dumps(response.json(), indent=4)
    pretty_json = json.dumps(response.json(), indent=4)
    pretty_json = json.dumps(response.json(), indent=4)
    print(pretty_json)  # Parse JSON response
else:
    print(f"Failed! Status Code: {response.status_code}")
pretty_json =  json.dumps(response.json(), indent=4)
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

print("Testing 1A")
print("Testing 2A")
print("Testing 3A")
print("Testing 4A")
print("Testing 5A")
print("Testing 6A")


def getusername():
    return "ujjwal_Thakur"
getusername()

def getpassword():
    return "ujjwal1234"



print("helloword")

def get_execution_time():
    import time
    start_time = time.time()
    # Simulate some processing
    time.sleep(2)  # Sleep for 2 seconds
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

get_execution_time()




for i in range(5):
    print(f"Iteration {i+1}: {get_execution_time()} seconds")

def(sdjasjdk)
print (ddddddddddddddddddd)