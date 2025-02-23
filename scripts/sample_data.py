# ShiftLogix/scripts/sample_data.py
# This script inserts sample data into the ShiftLogix database.

import sys
import os
from datetime import datetime

# Append 'backend' directory to sys.path so Python can find the 'app' package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary modules
from backend.app import create_app, db  # Import Flask app factory and database instance
from backend.app.models import Employee, Timesheet, Shift  # Ensure Shift is also imported

# Create the Flask app instance
app = create_app()

def insert_sample_data():
    """Inserts sample employee, shift, and timesheet data into the ShiftLogix database."""
    print("Inserting sample data into ShiftLogix database...")

    # Ensure database operations run within the Flask app context
    with app.app_context():  # FIX: Wrap database operations in the app context
        
        # ------------------------------ #
        # INSERT SAMPLE EMPLOYEES
        # ------------------------------ #
        
        # Check if Employee Alice exists before inserting
        emp1 = Employee.query.filter_by(email="alice@example.com").first()
        if not emp1:
            emp1 = Employee(name="Alice Johnson", email="alice@example.com", 
                            password_hash="hashedpassword1", role="Employee")
            db.session.add(emp1)

        # Check if Employee Bob exists before inserting
        emp2 = Employee.query.filter_by(email="bob@example.com").first()
        if not emp2:
            emp2 = Employee(name="Bob Smith", email="bob@example.com", 
                            password_hash="hashedpassword2", role="Employee")  # ✅ Changed from 'Scheduler' to 'Employee'
            db.session.add(emp2)

        db.session.commit()  # Commit employees to obtain their IDs

        # ------------------------------ #
        # INSERT SAMPLE SHIFT (If not exists)
        # ------------------------------ #
        
        shift1 = Shift.query.filter_by(employee_id=emp1.id, shift_date=datetime(2025, 2, 15).date()).first()
        if not shift1:
            shift1 = Shift(
                employee_id=emp1.id,
                employee_name=emp1.name,  # ✅ Store employee's name
                shift_date=datetime(2025, 2, 15).date(),  
                shift_start=datetime(2025, 2, 15, 9, 0, 0).time(),  
                shift_end=datetime(2025, 2, 15, 17, 0, 0).time()
            )
            db.session.add(shift1)
            db.session.commit()  # ✅ Commit the shift to the database

        # ------------------------------ #
        # INSERT SAMPLE TIMESHEET ENTRY (If not exists)
        # ------------------------------ #
        
        timesheet1 = Timesheet.query.filter_by(employee_id=emp1.id).first()
        if not timesheet1:
            timesheet1 = Timesheet(employee_id=emp1.id, clock_in=datetime(2025, 2, 15, 9, 0, 0))
            db.session.add(timesheet1)
            db.session.commit()  # Commit the timesheet entry to the database

        print("Sample data inserted successfully.")

# ------------------------------ #
# EXECUTION CHECK (RUN SCRIPT)
# ------------------------------ #

if __name__ == "__main__":
    with app.app_context():  # FIX: Ensure app context is active when running the script
        insert_sample_data()
