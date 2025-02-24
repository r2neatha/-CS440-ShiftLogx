"""
File: backend/app/routes/clock.py
Purpose: Defines the clock view for ShiftLogix/clock and the clock in function within.
"""

import os
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.models import Employee
from backend.app.validators.clock_validator import validate_clock

# Set the template directory to the frontend/route_templates folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../frontend/route_templates"))

# Create a Blueprint for clock routes with the URL prefix "/clock"
clock_bp = Blueprint("clock", __name__, url_prefix="/clock", template_folder=template_dir)

@clock_bp.route("/", methods=["GET", "POST"])
def clock():
    if request.method == "GET":
        return render_template("clock.html")
    else:
        userId = request.form.get("userId")
        password = request.form.get("password")
        action = request.form.get("action")
        
        is_valid, message = validate_clock(userId, password)
        if not is_valid:
            flash(message, "error")
            return redirect(url_for("clock.clock"))
        
        userId_int = int(userId)
        employee = Employee.query.filter_by(userId=userId_int).first()
        if not employee:
            flash("Invalid UserId.", "error")
            return redirect(url_for("clock.clock"))
        
        if not employee.check_password(password):
            flash("Invalid password.", "error")
            return redirect(url_for("clock.clock"))
        
        if action == "clock_in":
            flash("Clocked in successfully!", "success")
        elif action == "clock_out":
            flash("Clocked out successfully!", "success")
        else:
            flash("Unknown action.", "error")
        
        return redirect(url_for("clock.clock"))

@clock_bp.route("/direct", methods=["POST"])
@jwt_required()
def clock_direct():
    """
    New endpoint that allows a logged-in user to clock in or out directly,
    without having to re-enter their userId and password.
    """
    current_user = get_jwt_identity()
    try:
        current_user = int(current_user)
    except ValueError:
        flash("Invalid token.", "error")
        return redirect(url_for("auth.login"))
    
    action = request.form.get("action")
    employee = Employee.query.get(current_user)
    if not employee:
        flash("Employee not found.", "error")
        return redirect(url_for("employee_dashboard.dashboard_view", user_id=current_user))
    
    if action == "clock_in":
        flash("Clocked in successfully!", "success")
    elif action == "clock_out":
        flash("Clocked out successfully!", "success")
    else:
        flash("Unknown action.", "error")
    
    return redirect(url_for("employee_dashboard.dashboard_view", user_id=current_user))
