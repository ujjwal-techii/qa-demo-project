# Code: Haseeb Mehraj
# Date: 21-03-2025

import json
import os.path
import pytest
import random
import string
import uuid
from automation_api_vms.utils.helper import *



# Session-level setup and teardown for test environment
@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("\nSETTING UP RESOURCES...")
    yield  # Runs test_Report after this point
    print("\nTEARING DOWN RESOURCES...")


# To import data for test_file
@pytest.fixture()
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "data", "test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data


# Create Password For SignUp
@pytest.fixture()
def generate_random_password():
    def _generate(length=12):
        required = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice("!@#$%^&*()")
        ]
        rest = random.choices(string.ascii_letters + string.digits + "!@#$%^&*()", k=length - 4)
        return ''.join(random.sample(required + rest, length))
    return _generate


# Create username for Signup/Login
@pytest.fixture()
def create_username(load_user_data, generate_random_password, api_client):
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"  # Generate Email Id
    user_data = load_user_data["new_user"]
    user_data["username"] = unique_email
    user_data["password"] = generate_random_password()
    with open(unique_email_path, "a") as file:  # Store email address in the File
        file.write(f"{unique_email}, {user_data['password']}\n")
    return user_data


# Method to Read Data from Unique_Email
def read_credentials(
        file_path=unique_email_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:  # Read credentials from unique_email.txt file.
            data = [tuple(line.strip().split(",", 1)) for line in file if "," in line]
            return [(email.strip(), password.strip()) for email, password in data]  # Remove extra spaces
    except FileNotFoundError:
        print("This File does not exist")
        return []


# Read Vendors Names from file
@pytest.fixture
def read_next_vendor():
    pos = int(open(POSITION_FILE).read().strip()) if os.path.exists(POSITION_FILE) else 0
    vendors = [line.strip().split(",")[0] for line in open(VENDOR_FILE, encoding="utf-8")]
    vendor = vendors[pos % len(vendors)]  # Cycle back to start when reaching the end
    open(POSITION_FILE, "w").write(str((pos + 1) % len(vendors)))
    return vendor


# Method to Generate Random IP
@pytest.fixture
def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


# Define a function to save username and token
def save_token(username, token, file_path="../test_Report/tokens.txt"):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directory exists
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"Username: {username}, Token: {token}\n")
    except Exception as e:
        print(f"Error saving token: {e}")


# Save username, password, and token in a JSON file inside a new directory
def save_credentials(username, password, token,
                     directory="/home/adam/PycharmProjects/backend-automation/automation_api_vms/data",

                     filename="credentials.json"):
    os.makedirs(directory, exist_ok=True)  # Check directory exits or not.
    file_path = os.path.join(directory, filename)  # Define the full file path

    # Check if file exists and load existing data
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    existing_data = []
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    new_entry = {"username": username, "password": password, "token": token}  # Append new data
    existing_data.append(new_entry)

    # Save updated data back to file
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4)
    print(f"Credentials saved successfully at: {file_path}")


#In this method we read the username password and token from json file for add cam all user at a time
def read_credentials_all_json():
    # Load JSON file from a specific path
    with open(credentials_path, "r") as file:
        credentials_list = json.load(file)
    # Convert list of dicts to list of tuples for parametrize
    test_data = [(item["username"], item["password"], item["token"]) for item in credentials_list]
    return test_data


# In this method we read the username password and token from json file for add cam one user one time
def read_credentials_json():
    # Load JSON file from a specific path
    with open(credentials_path, "r") as file:
        credentials_list = json.load(file)
    # Return only the first set of credentials as a list with one tuple
    first_user = credentials_list[0]
    return [(first_user["username"], first_user["password"], first_user["token"])]


# Provides a valid login payload for authentication tests
@pytest.fixture
def valid_login_payload():
    return {"username": "Testuser1", "password": "Password123#"}


# Sends a login request with valid credentials and returns the response
@pytest.fixture
def response_valid_login(api_client, valid_login_payload):
    return api_client.post("auth/user/login", valid_login_payload)


@pytest.fixture
def invalid_payload():
    return {"username": "8dcfb966@123.com", "password": "password123"}


# Returns an invalid login payload for negative test scenarios
@pytest.fixture
def empty_credentials():
    return {"username": "", "password": ""}


# In this method we generate the payload for addcam api
@pytest.fixture
def generate_payload(read_next_vendor, generate_random_ip):
    def _make_payload(username, password):
        return {
            "cam_username": username,
            "cam_password": password,
            "vendor": read_next_vendor,
            "cam_ip": generate_random_ip
        }

    return _make_payload


# This method is used for remove the username in json file after logout
def remove_user_from_credentials(username_to_remove,
                                 file_path=credentials_path):
    with open(file_path, "r") as file:
        credentials = json.load(file)
    # Filter out the user
    updated_credentials = [user for user in credentials if user["username"] != username_to_remove]
    # Overwrite the file with the updated list
    with open(file_path, "w") as file:
        json.dump(updated_credentials, file, indent=4)
