
import unittest
from backend.app import create_app, db
from backend.app.models import Employee, Timesheet, Shift

#This file tests the /auth/login endpoint, checking for missing fields, invalid credentials, and valid login.

class AuthenticationEndpointTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test Flask application configured for testing
        self.app = create_app()
        self.app.config['TESTING'] = True
        # Use an in-memory SQLite database for faster tests
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        
        # Set up the database and add a dummy employee record for testing
        with self.app.app_context():
            db.drop_all() # added big fix
            db.create_all()
            # Create a dummy employee with known credentials
            employee = Employee(name="Test User", email="test@example.com", password_hash="secret", role="Employee")
            db.session.add(employee)
            db.session.commit()

    def tearDown(self):
        # Clean up the database after each test to prevent data leakage
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_missing_fields(self):
        # Test login endpoint with missing email and password
        response = self.client.post('/auth/login', json={})
        # Expect HTTP 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

    def test_login_invalid_credentials(self):
        # Test login endpoint with invalid credentials
        response = self.client.post('/auth/login', json={"email": "wrong@example.com", "password": "wrong"})
        # Expect HTTP 401 (Unauthorized)
        self.assertEqual(response.status_code, 401)

    def test_login_valid_credentials(self):
        # Test login endpoint with valid credentials
        response = self.client.post('/auth/login', json={"email": "test@example.com", "password": "secret"})
        # Expect HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        # Check that the response contains an "employee_id" field
        self.assertIn("employee_id", data)

if __name__ == "__main__":
    unittest.main()
