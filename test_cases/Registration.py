
import requests

def test_register_user():
    url = "https://dummyapi.com/register"  # Replace with your actual URL

    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "StrongPassword123",
        "phone": "9876543210"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    # ✅ Assertions
    assert response.status_code == 201 or response.status_code == 200
    assert "token" in response.json() or "id" in response.json()


if __name__ == "__main__":
    try:
        test_register_user()
        print("✅ Registration test passed")
    except AssertionError:
        print


print("check on")