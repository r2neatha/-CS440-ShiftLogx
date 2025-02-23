"""
File: scripts/reset_database.py
Purpose: Drops all tables, recreates them, and ensures a clean database reset.
"""

import sys
import os

# Ensure ShiftLogix is the root directory for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app import create_app, db
from sqlalchemy import text  # ✅ Allows executing raw SQL

# Create Flask app instance
app = create_app()

def reset_database():
    """
    Drops all tables safely, ensuring foreign key constraints are handled correctly.
    """
    with app.app_context():
        print("Disabling foreign key checks...")
        db.session.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))  # ✅ Temporarily disable foreign key checks

        print("Dropping all tables...")
        db.drop_all()  # ✅ Deletes all tables

        print("Re-enabling foreign key checks...")
        db.session.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))  # ✅ Re-enable foreign key checks
        db.session.commit()  # ✅ Commit changes

        print("Recreating tables...")
        db.create_all()  # ✅ Recreates tables

        print("Database has been successfully reset.")

if __name__ == "__main__":
    reset_database()
