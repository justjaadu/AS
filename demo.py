from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from collections import defaultdict

app = Flask(__name__)


# Hardcoded credentials
correct_username = "User1234"
correct_password = "abaaa"

# Dictionary to keep track of failed login attempts
failed_attempts = defaultdict(list)


# Function to record a failed login attempt
def record_failed_attempt(username):
    failed_attempts[username].append(datetime.now())

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

   
    if username == correct_username and password == correct_password:
        # Clear failed attempts after a successful login
        if username in failed_attempts:
            del failed_attempts[username]
        return jsonify({"message": "Access granted"}), 200
    else:
        record_failed_attempt(username)
        return jsonify({"message": "Access denied"}), 403

if __name__ == '__main__':
    app.run(debug=True)
