
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






def getusername():
    return "ujjwal_Thakur"
getusername()

def getpassword():
    return "ujjwal_Thakur@123"
getpassword()

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



print ("new code start ")



def reverse_string(s):
    return s[::-1]

reverse_string("Automation")





