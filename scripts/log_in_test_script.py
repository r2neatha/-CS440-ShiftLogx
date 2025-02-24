"""
File: scripts/log_in_test_script.py
Purpose: Tests authentication by logging in with a sample employee.
"""

import requests

# Define the base URL of your Flask app
BASE_URL = "http://127.0.0.1:5000"  # Adjust if running on a different host

# Sample login credentials
login_data = {
    "email": "test@example.com",
    "password": "Test123"
}

# Send POST request to login
response = requests.post(f"{BASE_URL}/login", json=login_data)

# Print response details
print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())
