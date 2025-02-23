import os
from flask import Blueprint, render_template, request, redirect, flash, url_for
from backend.app.models import Employee
from backend.app.validators.clock_validator import validate_clock

# Set the template directory to the frontend/route_templates folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../frontend/route_templates"))

# Create a Blueprint for clock routes with the URL prefix "/clock"
clock_bp = Blueprint("clock", __name__, url_prefix="/clock", template_folder=template_dir)

@clock_bp.route("/", methods=["GET", "POST"])
def clock():
    if request.method == "GET":
        # Render the clock.html template on GET
        return render_template("clock.html")
    else:
        # Retrieve form data
        userId = request.form.get("userId")
        password = request.form.get("password")
        action = request.form.get("action")
        
        # Validate form input using the validator
        is_valid, message = validate_clock(userId, password)
        if not is_valid:
            flash(message, "error")
            return redirect(url_for("clock.clock"))
        
        # Convert userId to integer (the validator has already ensured it is numeric)
        userId_int = int(userId)
        
        # Retrieve the employee record
        employee = Employee.query.filter_by(userId=userId_int).first()
        if not employee:
            flash("Invalid UserId.", "error")
            return redirect(url_for("clock.clock"))
        
        # Verify the password
        if not employee.check_password(password):
            flash("Invalid password.", "error")
            return redirect(url_for("clock.clock"))
        
        # Process the clock action based on the button clicked
        if action == "clock_in":
            flash("Clocked in successfully!", "success")
        elif action == "clock_out":
            flash("Clocked out successfully!", "success")
        else:
            flash("Unknown action.", "error")
        
        return redirect(url_for("clock.clock"))
