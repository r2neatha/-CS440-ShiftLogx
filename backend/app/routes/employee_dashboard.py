"""
File: backend/app/routes/employee_dashboard.py
Purpose: Defines the employee dashboard view for ShiftLogix.
"""
import os
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.models import Employee  # Import the Employee model

# Get absolute path for the frontend template folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../frontend/route_templates"))

employee_dashboard_bp = Blueprint("employee_dashboard", __name__, template_folder=template_dir)

@employee_dashboard_bp.route("/<int:user_id>/dashboard", methods=["GET"])
@jwt_required()
def dashboard_view(user_id):
    current_user = get_jwt_identity()
    try:
        current_user = int(current_user)
    except ValueError:
        flash("Invalid token.", "error")
        return redirect(url_for("auth.login"))

    if current_user != user_id:
        flash("Unauthorized access.")
        return redirect(url_for("home.home"))

    # Retrieve employee details
    employee = Employee.query.get(user_id)
    if not employee:
        flash("Employee not found.")
        return redirect(url_for("home.home"))
    
    # Placeholder for total hours (this pay period)
    total_hours = "40"  # Replace with an actual calculation if needed

    # Use employee.role as a stand-in for position; adjust as necessary.
    position = employee.role
    # Placeholder for rate; replace with actual data when available.
    rate = "15.00"

    return render_template(
        "employee_dashboard.html", 
        employee=employee, 
        total_hours=total_hours, 
        position=position, 
        rate=rate, 
        current_user=current_user
    )

