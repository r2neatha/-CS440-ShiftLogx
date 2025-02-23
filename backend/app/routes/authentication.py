"""
File: ShiftLogix/backend/app/routes/authentication.py
Purpose: Handles user authentication, including login and JWT token generation.
"""

# ADDED: Import additional functions from Flask needed for template rendering and redirects.
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from backend.app.validators.log_in_validator import validate_log_in  # Import login validator
from backend.app.models import Employee  # Import Employee model
from backend.app import db  # Import database instance

# Create Blueprint for authentication routes
auth_bp = Blueprint("auth", __name__)

# ------------------------------ #
# USER LOGIN ENDPOINT
# Authenticates user and returns JWT token
# ------------------------------ #
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Handles rendering and processing of the login page.
    
    GET:
      - ADDED: Renders the login page template (login.html) which contains the login form.
      
    POST:
      - Processes login credentials submitted via the form.
      - Supports both JSON (e.g., from an API client) and form-encoded data (from the login page).
      - Validates the email and password using the log_in_validator.
      - CHANGED: If validation fails, flashes an error and redirects back to the login page.
      - If successful, generates a JWT token and returns a JSON response with the token.
    """
    # ADDED: Handle GET request to render the login form.
    if request.method == "GET":
        return render_template("login.html")
    
    # CHANGED: Handle POST request to support both JSON and form data.
    data = request.get_json() if request.is_json else request.form
    email = data.get("email")
    password = data.get("password")
    
    # Validate login credentials using the provided validator function.
    valid, message = validate_log_in(email, password)
    if not valid:
        flash("Invalid email or password. Please try again.", "error")
        return redirect(url_for("auth.login"))
    
    # Check if the employee exists in the database and verify the password.
    user = Employee.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        flash("Invalid credentials. Please check your email and password.", "error")
        return redirect(url_for("auth.login"))
    
    # Generate a JWT token valid for 1 hour.
    access_token = create_access_token(identity=email, expires_delta=timedelta(hours=1))
    
    # CHANGED: For API clients, return a JSON response with the token.
    return jsonify({"access_token": access_token}), 200