from app import db

# Employee Table
class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum("Employee", "Scheduler", "Admin"), nullable=False)

    # Define relationships with explicit foreign keys
    shifts = db.relationship("Shift", foreign_keys="[Shift.employee_id]", backref="assigned_employee", lazy=True)
    scheduled_shifts = db.relationship("Shift", foreign_keys="[Shift.scheduler_id]", backref="scheduler", lazy=True)
    timesheets = db.relationship("Timesheet", backref="employee", lazy=True)

# Shift Table
class Shift(db.Model):
    __tablename__ = "shifts"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    scheduler_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=True)  # Nullable for auto-assignments
    scheduled_start = db.Column(db.DateTime, nullable=False)
    scheduled_end = db.Column(db.DateTime, nullable=False)

# Timesheet Table
class Timesheet(db.Model):
    __tablename__ = "timesheets"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    clock_in = db.Column(db.DateTime, nullable=False)
    clock_out = db.Column(db.DateTime)
    total_hours = db.Column(db.Float)
