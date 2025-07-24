import random
import time
import logging
import json
from typing import List, Dict

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# ------------------ Dummy Data Generator ------------------ #
class DummyDataGenerator:
    def __init__(self, count: int):
        self.count = count

    def generate_user(self, id: int) -> Dict:
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
        return {
            "id": id,
            "name": random.choice(names),
            "age": random.randint(18, 65),
            "email": f"user{id}@example.com",
            "is_active": bool(random.getrandbits(1)),
            "roles": random.sample(["admin", "user", "editor", "viewer"], k=random.randint(1, 3))
        }

    def generate_users(self) -> List[Dict]:
        return [self.generate_user(i) for i in range(1, self.count + 1)]


# ------------------ Dummy API Simulation ------------------ #
class DummyAPI:
    def __init__(self):
        self.database = {}

    def create_user(self, user_data: Dict) -> Dict:
        logging.info(f"Creating user: {user_data['name']}")
        self.database[user_data["id"]] = user_data
        return {"status": "success", "message": "User created", "user": user_data}

    def get_user(self, user_id: int) -> Dict:
        user = self.database.get(user_id)
        if user:
            logging.info(f"User found: {user}")
            return {"status": "success", "user": user}
        else:
            logging.warning(f"User ID {user_id} not found.")
            return {"status": "error", "message": "User not found"}

    def delete_user(self, user_id: int) -> Dict:
        if user_id in self.database:
            del self.database[user_id]
            logging.info(f"Deleted user ID {user_id}")
            return {"status": "success", "message": "User deleted"}
        else:
            return {"status": "error", "message": "User not found"}

    def list_users(self) -> List[Dict]:
        return list(self.database.values())


# ------------------ File Operations ------------------ #
def save_to_file(data, filename: str):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving to file: {e}")


def load_from_file(filename: str) -> List[Dict]:
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        logging.info(f"Data loaded from {filename}")
        return data
    except FileNotFoundError:
        logging.warning(f"{filename} not found.")
        return []


# ------------------ Utility Functions ------------------ #
def simulate_delay(seconds: int = 1):
    logging.info(f"Simulating delay for {seconds} seconds...")
    time.sleep(seconds)


# ------------------ Main Logic ------------------ #
def main():
    logging.info("Starting dummy script...")
    generator = DummyDataGenerator(count=10)
    api = DummyAPI()

    users = generator.generate_users()
    simulate_delay(2)

    for user in users:
        result = api.create_user(user)
        logging.debug(result)

    simulate_delay()

    logging.info("Listing all users...")
    all_users = api.list_users()
    print(f"Total Users: {len(all_users)}")

    save_to_file(all_users, "dummy_users.json")

    simulate_delay()

    logging.info("Fetching a single user...")
    response = api.get_user(5)
    print(response)

    simulate_delay()

    logging.info("Deleting user ID 3...")
    print(api.delete_user(3))

    simulate_delay()

    logging.info("Loading users from file...")
    loaded_users = load_from_file("dummy_users.json")
    print(f"Loaded Users: {len(loaded_users)}")


if __name__ == "__main__":
    main()


print("check on")
print("check on 111")