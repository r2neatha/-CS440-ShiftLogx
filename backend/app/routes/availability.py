"""
File: backend/app/routes/availability.py
Purpose: Defines the availability view for ShiftLogix.
"""
import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from backend.app.models import Availability
from backend.app import db

# Get absolute path for the frontend template folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../frontend/route_templates"))

availability_bp = Blueprint("availability", __name__, template_folder=template_dir)

@availability_bp.route("/<int:user_id>/availability", methods=["GET", "POST"])
@jwt_required()
def availability_view(user_id):
    current_user = int(get_jwt_identity())
    if current_user != user_id:
        flash("Unauthorized access.")
        return redirect(url_for("home.home"))
    
    if request.method == "POST":
        # Get form data
        day_of_week = request.form.get("day_of_week")
        available_start = request.form.get("available_start")
        available_end = request.form.get("available_end")
        
        # Convert the time strings to time objects (expected format: HH:MM)
        try:
            available_start_time = datetime.strptime(available_start, "%H:%M").time()
            available_end_time = datetime.strptime(available_end, "%H:%M").time()
        except ValueError:
            flash("Invalid time format. Please use HH:MM.")
            return redirect(url_for("availability.availability_view", user_id=user_id))
        
        # Check if a record for this user and day already exists
        record = Availability.query.filter_by(employee_id=user_id, day_of_week=day_of_week).first()
        if record:
            record.available_start = available_start_time
            record.available_end = available_end_time
        else:
            new_record = Availability(
                employee_id=user_id,
                day_of_week=day_of_week,
                available_start=available_start_time,
                available_end=available_end_time
            )
            db.session.add(new_record)
        
        db.session.commit()
        flash("Availability updated successfully.")
        return redirect(url_for("availability.availability_view", user_id=user_id))
    
    # For GET requests, retrieve the current availability for the user
    availabilities = Availability.query.filter_by(employee_id=user_id).all()
    return render_template("availability.html", availabilities=availabilities, current_user=current_user)
