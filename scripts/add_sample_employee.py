"""
File: scripts/add_sample_employee.py
Purpose: Inserts a sample employee into the database for authentication testing.
"""

import sys
import os

# Append project path to sys.path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app import create_app, db
from backend.app.models import Employee

# Create Flask app instance
app = create_app()

def add_sample_employee():
    """
    Adds a sample employee to the database for testing login functionality.
    """
    with app.app_context():
        # Check if the test employee already exists
        existing_user = Employee.query.filter_by(email="test@example.com").first()
        if existing_user:
            print("Test employee already exists.")
            return
        
        # Create new employee
        test_employee = Employee(
            userId=1,
            first_name="John",
            last_name="Doe",
            email="test@example.com",
            role="Employee"
        )

        # Set hashed password
        test_employee.set_password("Test123")

        # Add to database
        db.session.add(test_employee)
        db.session.commit()
        print("Sample employee added successfully.")

if __name__ == "__main__":
    add_sample_employee()
