"""
File: ShiftLogix/backend/app/routes/authentication.py
Purpose: Handles user authentication, including login and JWT token generation.
"""

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity
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
      - Renders the login page template (login.html) which contains the login form.
      
    POST:
      - Processes login credentials submitted via the form.
      - Supports both JSON (e.g., from an API client) and form-encoded data (from the login page).
      - Validates the email and password using the log_in_validator.
      - If validation fails, flashes an error and redirects back to the login page.
      - If successful, generates a JWT token with the employee's userId as identity.
      - For JSON requests, returns a JSON response with the token.
      - For form submissions, sets the token as a cookie and redirects the user to their dashboard.
    """
    if request.method == "GET":
        return render_template("login.html")
    
    data = request.get_json() if request.is_json else request.form
    email = data.get("email")
    password = data.get("password")
    
    # Validate login credentials
    valid, message = validate_log_in(email, password)
    if not valid:
        flash("Invalid email or password. Please try again.", "error")
        return redirect(url_for("auth.login"))
    
    # Check if the employee exists and verify the password.
    user = Employee.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        flash("Invalid credentials. Please check your email and password.", "error")
        return redirect(url_for("auth.login"))
    
    # Generate a JWT token with the employee's userId as identity.
    access_token = create_access_token(
        identity=str(user.userId), 
        expires_delta=timedelta(hours=1)
    )

    
    # For JSON requests, return the token as JSON.
    if request.is_json:
        return jsonify({"access_token": access_token}), 200
    else:
        # For form-based logins, set the token as an HTTP-only cookie and redirect to dashboard.
        response = redirect(url_for("employee_dashboard.dashboard_view", user_id=user.userId))
        set_access_cookies(response, access_token)
        return response
