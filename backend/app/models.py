"""
File: ShiftLogix/backend/app/models.py
Purpose: Defines database models, including Employee authentication.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt  # Import for password hashing
from backend.app import db

bcrypt = Bcrypt()  # Initialize Bcrypt for password hashing

# ------------------------------ #
# EMPLOYEE MODEL
# Stores employee authentication and role data
# ------------------------------ #
class Employee(db.Model):
    __tablename__ = "employees"
    __table_args__ = {'extend_existing': True}  # Prevent duplicate definitions

    userId = db.Column(db.Integer, primary_key=True)  # Unique Employee ID
    first_name = db.Column(db.String(100), nullable=False)  # First Name
    last_name = db.Column(db.String(100), nullable=False)  # Last Name
    email = db.Column(db.String(100), unique=True, nullable=False)  # Unique Email Address
    password_hash = db.Column(db.String(255), nullable=False)  # Secure Hashed Password
    role = db.Column(db.String(50), nullable=False)  # Role of the Employee (Admin, Employee, etc.)

    def set_password(self, password):
        """Hashes password and stores it securely."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Verifies the provided password against the stored hash."""
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Employee {self.userId}: {self.first_name} {self.last_name} ({self.role})>"
