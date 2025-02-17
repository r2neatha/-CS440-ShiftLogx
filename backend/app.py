from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()  # Ensure PyMySQL is recognized

# Initialize Flask App
app = Flask(__name__)

# MySQL Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://shiftlogix_user:AdminPassword1234@localhost/shiftlogix"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Database
db = SQLAlchemy(app)

# Ensure API is working
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "ShiftLogix API is running"}), 200

# GET all employees
@app.route("/employees", methods=["GET"])
def get_employees():
    from models import Employee  # Import models inside routes to avoid circular imports
    employees = Employee.query.all()
    return jsonify([{"id": emp.id, "name": emp.name, "email": emp.email, "role": emp.role} for emp in employees])

# GET all shifts
@app.route("/shifts", methods=["GET"])
def get_shifts():
    from models import Shift  # Import model
    shifts = Shift.query.all()
    return jsonify([
        {"id": shift.id, "employee_id": shift.employee_id, "scheduler_id": shift.scheduler_id,
         "scheduled_start": shift.scheduled_start, "scheduled_end": shift.scheduled_end}
        for shift in shifts
    ])

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
