"""
File: backend/app/routes/schedule.py
Purpose: Defines the schedule view for ShiftLogix.
"""
import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.models import Shift  # Import your Shift model

# Get absolute path for the frontend template folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../frontend/route_templates"))

schedule_bp = Blueprint("schedule", __name__, template_folder=template_dir)

@schedule_bp.route("/<int:user_id>/schedule", methods=["GET", "POST"])
@jwt_required()
def schedule_view(user_id):
    current_user = int(get_jwt_identity())
    if current_user != user_id:
        flash("Unauthorized access.")
        return redirect(url_for("home.home"))
    
    if request.method == "POST":
        # Process add/drop shift request
        shift_id = request.form.get("shift_id")
        action = request.form.get("action")
        reason = request.form.get("reason")
        
        # TODO: Add logic to store the request in the drop request table (not implemented yet)
        flash("Your shift request has been submitted.")
        return redirect(url_for("schedule.schedule_view", user_id=user_id))
    
    # Retrieve the weekly schedule for the logged-in user
    shifts = Shift.query.filter_by(employee_id=user_id).all()
    return render_template("schedule.html", shifts=shifts, current_user=current_user)
