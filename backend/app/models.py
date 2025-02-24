"""
File: ShiftLogix/backend/app/models.py
Purpose: Defines database models, including Employee authentication.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from backend.app import db

bcrypt = Bcrypt()

# ------------------------------ #
# EMPLOYEE MODEL
# ------------------------------ #
class Employee(db.Model):
    __tablename__ = "employees"
    __table_args__ = {'extend_existing': True}

    userId = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Employee {self.userId}: {self.first_name} {self.last_name} ({self.role})>"

# ------------------------------ #
# SHIFT MODEL (Stores employee shift schedules)
# ------------------------------ #
class Shift(db.Model):
    __tablename__ = "shifts"

    shiftId = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.userId"), nullable=False)
    scheduled_start = db.Column(db.DateTime, nullable=False)
    scheduled_end = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return (f"<Shift {self.shiftId} for Employee {self.employee_id} "
                f"from {self.scheduled_start} to {self.scheduled_end}>")

# ------------------------------ #
# TIMESHEET MODEL (Tracks employee clock-in and clock-out times)
# ------------------------------ #
class Timesheet(db.Model):
    __tablename__ = "timesheets"

    timesheetId = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.userId"), nullable=False)
    clock_in = db.Column(db.DateTime, nullable=False)
    clock_out = db.Column(db.DateTime, nullable=True)  # Allow null until clock-out

    def __repr__(self):
        return f"<Timesheet {self.timesheetId} for Employee {self.employee_id} (Clock-in: {self.clock_in})>"

# ------------------------------ #
# AVAILABILITY MODEL (Stores employee availability)
# ------------------------------ #
class Availability(db.Model):
    __tablename__ = "availability"

    availabilityId = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.userId"), nullable=False)
    day_of_week = db.Column(db.String(10), nullable=False)  # e.g., 'Monday'
    available_start = db.Column(db.Time, nullable=False)
    available_end = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return (f"<Availability {self.availabilityId} for Employee {self.employee_id} "
                f"on {self.day_of_week} from {self.available_start} to {self.available_end}>")

# ------------------------------ #
# SHIFT CHANGE MODEL (Handles shift change requests)
# ------------------------------ #
class ShiftChange(db.Model):
    __tablename__ = "shift_change"

    id = db.Column(db.Integer, primary_key=True)  # Primary key for each shift change request.
    shift_id = db.Column(db.Integer, db.ForeignKey("shifts.shiftId"), nullable=False)
    # 'add_or_drop' indicates the type of change: either "add" or "drop".
    add_or_drop = db.Column(db.String(10), nullable=False)
    # References the employee making the request.
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.userId"), nullable=False)
    # 'reason' provides details about why the change is being requested.
    reason = db.Column(db.Text, nullable=True)
    # 'status' tracks the state of the request (e.g., pending, approved, denied).
    status = db.Column(db.String(20), nullable=False, default="pending")

    def __repr__(self):
        return (f"<ShiftChange id={self.id} shift_id={self.shift_id} action={self.add_or_drop} "
                f"employee_id={self.employee_id} status={self.status}>")
