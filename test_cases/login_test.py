import requests

def test_login_valid_user():
    url = "https://example.com/api/login"
    payload = {
        "email": "test@example.com",
        "password": "Password123"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert "token" in response.json()
