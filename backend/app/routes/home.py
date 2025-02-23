"""
File: backend/app/routes/home.py
Purpose: Defines the home page view for ShiftLogix.
"""
import os
from flask import Blueprint, render_template

# Get absolute path for the frontend template folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../frontend/route_templates"))

home_bp = Blueprint("home", __name__, template_folder=template_dir)

@home_bp.route("/")
def home():
    return render_template("home.html")  # Flask should now find it
