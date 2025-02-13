from app import db
from models import Employee, Shift, Timesheet

def reset_database():
    print("Dropping all tables...")
    db.drop_all()  # Delete existing tables

    print("Recreating tables...")
    db.create_all()  # Recreate tables

    print("Database reset successfully.")

if __name__ == "__main__":
    with db.session.begin():
        reset_database()
