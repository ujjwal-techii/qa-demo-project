import time
import requests



class APIClient:
    def __init__(self):
        self.BASE_URL = "http://192.168.119.199:8000"
        self.headers = {
            "Content-Type": "application/json",
            "server": "uvicorn"
        }

    def post(self, endpoint, data, token=None, max_retry_duration=360):  # 6 minutes = 360 seconds
        url = f"{self.BASE_URL}/{endpoint}"
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

        start_time = time.time()

        while True:
            try:
                response = requests.post(url, headers=self.headers, json=data)

                if response.status_code == 429:
                    retry_after = int(response.headers.get("Retry-After", 2))
                    print(f"[429] Too Many Requests. Retrying in {retry_after} seconds...")

                    if time.time() - start_time + retry_after > max_retry_duration:
                        print("[Timeout] Retry limit of 6 minutes reached.")
                        return response  # return even if still 429

                    time.sleep(retry_after)
                else:
                    return response  # success or other status

            except requests.exceptions.RequestException as e:
                print(f"[Request Error] {e}")
                if time.time() - start_time + 2 > max_retry_duration:
                    print("[Timeout] Retry limit of 6 minutes reached due to network errors.")
                    return None
                time.sleep(2)
