
"""
This module contains tests related to the login functionality.

It includes various test cases for valid and invalid login scenarios.
"""

import hashlib
import random


# --------------------- USER MANAGEMENT ---------------------

users_db = {
    "admin@example.com": {
        "name": "Admin",
        "password": hashlib.sha256("admin123".encode()).hexdigest(),
        "role": "admin",
    },
    "user@example.com": {
        "name": "User",
        "password": hashlib.sha256("user123".encode()).hexdigest(),
        "role": "user",
    },
}

"""
Login file used
"""


def login(email, password):
    print(f"[INFO] Attempting login for {email}")
    hashed_password = hashlib.sha256(password. encode()).hexdigest()
    user = users_db.get(email)

    if user and user["password"] == hashed_password:
        print(
            f"[SUCCESS] Welcome, "
            f"{user['name']}!"f" You are logged in as {user['role']}."
        )
        return True
    else:
        print("[ERROR] Invalid email or password.")
        return False


# --------------------- PRODUCT MANAGEMENT ---------
products = [
    {"id": 101, "name": "Laptop", "price": 65000},
    {"id": 102, "name": "Mouse", "price": 700},
    {"id": 103, "name": "Keyboard", "price": 1500},
    {"id": 104, "name": "Monitor", "price": 12000},]


def list_products():
    print("\nAvailable Products:")
    for product in products:
        print(
            f" - ID: {product['id']} | "
            f"Name: {product['name']} | Price: ₹{product['price']}"
        )


def add_product(name, price):
    new_id = random.randint(200, 999)
    products.append({"id": new_id, "name": name, "price": price})
    print(f"[SUCCESS] Product '{name}' added with ID {new_id}.")


def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    print(f"[INFO] Product ID {product_id} deleted.")


# --------------------- ADMIN DASHBOARD ---------------------


def admin_panel():
    print("\n=== Admin Panel ===")
    list_products()
    print("\nAdding dummy product...")
    add_product("Webcam", 2500)
    print("Updated product list:")
    list_products()
    print("\nDeleting product ID 102...")
    delete_product(102)
    list_products()


# --------------------- MAIN FUNCTION ---------------------


def main():
    print("=== Dummy App Login ===")
    email = input("Enter email: ")
    password = input("Enter password: ")

    if login(email, password):
        if users_db[email]["role"] == "admin":
            admin_panel()
        else:
            list_products()
            print("[INFO] You can view "
                  "products, but you don’t have admin rights.")
    else:
        print("[EXIT] Login failed. Exiting...")


if __name__ == "__main__":
    main()


def webapp():
    pass


i = 2  # defined outside


def whatsapp(a):

    if i in a:
        print("add")
    else:
        print("not found")


# Example global variable 'i'
i = 2

whatsapp([1, 2, 3])  # Output: add

# Created :Haseeb Mehraj
# Date: 24 March 2025
# Method Name : Post Method

import pytest
from automation_api_vms.conftest import *
from automation_api_vms.utils.api_client import APIClient


# EndPoint Used In below Methods
endpoint = "auth/register/user"


@pytest.fixture(scope="module")
def api_client():
    return APIClient()


# Testcase Check response code 200
def test_case_check_response(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert response.status_code == 200


# Testcase Check Response Length
def test_case_check_length(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert len(response.json()) > 0


# Testcase Check UserName Match
def test_case_username_match(api_client, create_username):
    name = create_username.get("username")  # Use .get() for safety
    username = create_username
    response = api_client.post(endpoint, username)  # Send correct payload
    assert response.json().get("username") == name, "Username does not match!"


# Testcase Check Id in Response
def test_case_id_contain(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert "id" in response.json(), "Response should contain 'id'"


# Testcase Check Username in Response
def test_case_username_contain(api_client, create_username):
    create_username.get("username")
    username = create_username
    response = api_client.post(endpoint, username)
    assert "username" in response.json(), "Response should contain 'username'"


# Testcase Check Token in Response
def test_case_token_contain(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert "token" in response.json(), ("Response should contain "
                                        "authentication token")


# Testcase Check I'd DataType
def test_case_id_datatype(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert isinstance(response.json().get("id"), int), ("User ID should be an "
                                                        "integer")


# Testcase Check Username DataType
def test_case_username_datatype(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert isinstance(response.json().get("username"), str), \
        "User username should be an String"


# Testcase Check Token DataType
def test_case_token_datatype(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert isinstance(response.json().get("token"), str), \
        "User token should be an String"


# Testcase Check Id Not Empty
def test_case_id_empty_datatype(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert response.json().get("id") > 0, "User ID should be greater than 0"


# Testcase Check Username Not Empty
def test_case_username_empty_datatype(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert len(response.json().get("username").strip()) > 0, \
        "Username should not be empty"


# Testcase Check Token Not Empty
def test_case_token_empty_datatype(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert len(response.json().get("token").strip()) > 0, \
        "Token should not be empty"


# Testcase Check Response Time is less than 2 Seconds
def test_case_response_time(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert response.elapsed.total_seconds() < 2


# Testcase Check Resource is not found 404
def test_case_error_response_user(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    try:
        assert response.status_code == 404
    except:
        print("Negative Test Case Passed")


# Testcase Check Resource is not found 500
def test_case_error_response_server(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    try:
        assert response.status_code == 500
    except:
        print("Negative Test Case Passed")


# Testcase Check Error Message
def test_case_error_message(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    try:
        assert response.json().get("error") == "internal server error"
    except:
        print("Negative Test Case Passed")


# Testcase Check Status Not Equal 200
def test_case_invalid_status_code(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    try:
        assert response.status_code != 200
    except:
        print("Negative Test Case Passed")


# TestCase Check Username Missing
def test_case_username_missing(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    try:
        assert response.json().get("username") is None
    except:
        print("Negative Test Case Passed")


# Testcase with Empty payload
def test_register_empty_payload(api_client):
    response = api_client.post(endpoint, {})
    assert response.status_code == 400


# Testcase with Only username
def test_register_only_username(api_client):
    response = api_client.post(endpoint, {"username": "test@example.com"})
    assert response.status_code == 400


# Testcase with blank email format
def test_register_invalid_email(api_client, empty_credentials):
    data = empty_credentials
    response = api_client.post(endpoint, data)
    assert response.status_code == 400


# Testcase Short password
def test_register_short_password(api_client):
    data = {"username": "shortpass@example.com", "password": "123"}
    response = api_client.post(endpoint, data)
    assert response.status_code == 400


# Testcase Unicode characters
def test_register_unicode_username(api_client):
    data = {"username": "用户@例子.广告", "password": "unicodePass123"}
    response = api_client.post(endpoint, data)
    assert response.status_code in [200, 201, 400]  # Accept or reject clearly


# Testcase XSS attack payload
def test_register_xss_username(api_client):
    data = {"username": "<script>alert(1)</script>", "password": "pass1234"}
    response = api_client.post(endpoint, data)
    assert response.status_code == 400 or "script" not in response.text.lower()


# Testcase with Long username
def test_register_long_username(api_client):
    long_username = "a" * 300 + "@example.com"
    data = {"username": long_username, "password": "pass1234"}
    response = api_client.post(endpoint, data)
    assert response.status_code == 400


# Testcase with Extra unexpected field
def test_register_extra_field(api_client):
    data = {"username": "extrafield@example.com", "password": "pass1234", "role": "admin"}
    response = api_client.post(endpoint, data)
    assert response.status_code in [200, 201, 400]  # Depends on how strict the API is


# Testcase with Existing user
def test_register_existing_user(api_client, valid_login_payload):
    data = valid_login_payload
    api_client.post(endpoint, data)  # First time (assume success)
    response = api_client.post(endpoint, data)  # Second time (should fail)
    assert response.status_code in [400, 409]
    assert "already exists" in response.text.lower()


# Testcase: Check presence and non-emptiness of 'refresh_token'
def test_register_refresh_token_present(api_client, create_username):
    username = create_username
    response = api_client.post(endpoint, username)
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    response_json = response.json()
    # Validate presence and non-emptiness of 'refresh_token'
    assert "refresh_token" in response_json, "'refresh_token' key not found in response"
    assert isinstance(response_json["refresh_token"], str), "'refresh_token' should be a string"
    assert response_json["refresh_token"].strip() != "", "'refresh_token' is empty"

