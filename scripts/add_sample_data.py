"""
File: scripts/add_sample_data.py
Purpose: Inserts sample data into the database for testing purposes.
         This script adds sample entries for Employee, Shift, Timesheet, and Availability tables.
"""

import sys
import os
from datetime import datetime, time

# Append the project path to sys.path so that imports work correctly.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Flask app factory, database, and models
from backend.app import create_app, db
from backend.app.models import Employee, Shift, Timesheet, Availability

# Create the Flask application instance using the factory function.
app = create_app()

def add_sample_employee():
    """
    Adds a sample employee to the database for testing.
    Returns the Employee object if added (or already exists), otherwise returns None.
    """
    try:
        # Check if the sample employee already exists to avoid duplicates.
        existing_user = Employee.query.filter_by(email="sample_employee@example.com").first()
        if existing_user:
            print("Sample employee already exists.")
            return existing_user

        # Create a new Employee instance with sample data.
        sample_emp = Employee(
            userId=1,  # You can allow auto-increment if preferred; here it's set explicitly.
            first_name="Alice",
            last_name="Smith",
            email="sample_employee@example.com",
            role="Employee"
        )
        # Set a hashed password using the provided helper method.
        sample_emp.set_password("SamplePass123")
        
        # Add the new employee to the session and commit it to the database.
        db.session.add(sample_emp)
        db.session.commit()
        print("Sample employee added successfully.")
        return sample_emp

    except Exception as e:
        # Rollback the session in case of an error to keep the database consistent.
        print(f"Failed to add sample employee. Error: {e}")
        db.session.rollback()
        return None

def add_sample_shift(employee):
    """
    Adds a sample shift for the provided employee.
    Returns the Shift object if added successfully.
    """
    try:
        # Check if a shift entry already exists for this employee.
        existing_shift = Shift.query.filter_by(employee_id=employee.userId).first()
        if existing_shift:
            print("Sample shift already exists for this employee.")
            return existing_shift

        # Create a new Shift instance with a sample start and end datetime.
        sample_shift = Shift(
            employee_id=employee.userId,
            scheduled_start=datetime(2025, 3, 10, 9, 0, 0),  # Year, Month, Day, Hour, Minute, Second
            scheduled_end=datetime(2025, 3, 10, 17, 0, 0)
        )
        # Add the shift to the session and commit it.
        db.session.add(sample_shift)
        db.session.commit()
        print("Sample shift added successfully.")
        return sample_shift

    except Exception as e:
        print(f"Failed to add sample shift. Error: {e}")
        db.session.rollback()
        return None

def add_sample_timesheet(employee):
    """
    Adds a sample timesheet entry for the provided employee.
    Returns the Timesheet object if added successfully.
    """
    try:
        # Check if a timesheet entry already exists for this employee.
        existing_timesheet = Timesheet.query.filter_by(employee_id=employee.userId).first()
        if existing_timesheet:
            print("Sample timesheet already exists for this employee.")
            return existing_timesheet

        # Create a new Timesheet instance with sample clock-in and clock-out times.
        sample_timesheet = Timesheet(
            employee_id=employee.userId,
            clock_in=datetime(2025, 3, 10, 9, 0, 0),
            clock_out=datetime(2025, 3, 10, 17, 0, 0)  # Clock-out can be null until the employee clocks out.
        )
        # Add the timesheet to the session and commit it.
        db.session.add(sample_timesheet)
        db.session.commit()
        print("Sample timesheet added successfully.")
        return sample_timesheet

    except Exception as e:
        print(f"Failed to add sample timesheet. Error: {e}")
        db.session.rollback()
        return None

def add_sample_availability(employee):
    """
    Adds a sample availability entry for the provided employee.
    Returns the Availability object if added successfully.
    """
    try:
        # Check if an availability record already exists for this employee.
        existing_availability = Availability.query.filter_by(employee_id=employee.userId).first()
        if existing_availability:
            print("Sample availability already exists for this employee.")
            return existing_availability

        # Create a new Availability instance.
        # Here, 'day_of_week' is set to 'Monday' and sample available times are provided.
        sample_availability = Availability(
            employee_id=employee.userId,
            day_of_week="Monday",
            available_start=time(8, 0, 0),  # Time when the employee becomes available.
            available_end=time(16, 0, 0)      # Time when the employee is no longer available.
        )
        # Add the availability record to the session and commit it.
        db.session.add(sample_availability)
        db.session.commit()
        print("Sample availability added successfully.")
        return sample_availability

    except Exception as e:
        print(f"Failed to add sample availability. Error: {e}")
        db.session.rollback()
        return None

def main():
    """
    Main function to add sample data to the database.
    It inserts data into Employee, Shift, Timesheet, and Availability tables,
    printing a success or failure message for each operation.
    """
    with app.app_context():
        # Add a sample employee first.
        employee = add_sample_employee()
        if employee is None:
            print("Aborting sample data insertion due to failure in adding the employee.")
            return
        
        # Add sample shift for the employee.
        shift = add_sample_shift(employee)
        # Add sample timesheet for the employee.
        timesheet = add_sample_timesheet(employee)
        # Add sample availability for the employee.
        availability = add_sample_availability(employee)
        
        print("\nSample data insertion complete.")
        if shift:
            print(f"Shift record: {shift}")
        if timesheet:
            print(f"Timesheet record: {timesheet}")
        if availability:
            print(f"Availability record: {availability}")

if __name__ == "__main__":
    main()
