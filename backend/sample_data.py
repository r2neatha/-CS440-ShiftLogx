from app import db
from models import Employee, Shift, Timesheet
from datetime import datetime

def insert_sample_data():
    print("Inserting sample data into ShiftLogix database...")

    # Create sample employees
    emp1 = Employee(name="Alice Johnson", email="alice@example.com", password_hash="hashedpassword1", role="Employee")
    emp2 = Employee(name="Bob Smith", email="bob@example.com", password_hash="hashedpassword2", role="Scheduler")

    # Add employees and commit so IDs are assigned
    db.session.add(emp1)
    db.session.add(emp2)
    db.session.commit()

    # Refresh objects to get IDs
    db.session.refresh(emp1)
    db.session.refresh(emp2)

    # Create sample shifts using assigned IDs
    shift1 = Shift(employee_id=emp1.id, scheduler_id=emp2.id, 
                   scheduled_start=datetime(2025, 2, 13, 9, 0, 0), 
                   scheduled_end=datetime(2025, 2, 13, 17, 0, 0))

    db.session.add(shift1)
    db.session.commit()

    # Create a sample timesheet record
    timesheet1 = Timesheet(employee_id=emp1.id, 
                           clock_in=datetime(2025, 2, 13, 9, 5, 0), 
                           clock_out=datetime(2025, 2, 13, 17, 0, 0), 
                           total_hours=7.92)

    db.session.add(timesheet1)
    db.session.commit()

    print("Sample data inserted successfully.")

if __name__ == "__main__":
    insert_sample_data()
