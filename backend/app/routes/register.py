"""
Register Route for ShiftLogix Application

Handles user registration by collecting user details,
validating input, hashing passwords, and storing them in the database.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from backend.app import db
from backend.app.models import Employee
from werkzeug.security import generate_password_hash

# Blueprint for registration route
register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles user registration.
    
    GET: Renders the registration form.
    POST: Processes the form, validates input, hashes password, 
          saves user to database, and redirects to login.
    """
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate inputs
        if not first_name or not last_name or not email or not password:
            flash("All fields are required!", "danger")
            return redirect(url_for('register.register'))

        # Check if user already exists
        existing_user = Employee.query.filter_by(email=email).first()
        if existing_user:
            flash("Email is already registered. Please log in.", "warning")
            return redirect(url_for('auth.login'))

        # Hash password before storing
        hashed_password = generate_password_hash(password)

        # Create new user
        new_user = Employee(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password_hash=hashed_password
        )

        # Add user to database
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')
