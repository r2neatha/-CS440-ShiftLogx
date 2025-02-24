"""
File: ShiftLogix/backend/app/__init__.py
Purpose: Initializes the Flask application, database, and registers Blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager  # Import JWT for authentication

# Initialize Flask extensions
db = SQLAlchemy()
jwt = JWTManager()  # Initialize JWT

def create_app():
    app = Flask(__name__)

    # Set a secret key for session management
    app.config["SECRET_KEY"] = "age0ijl6uc0wve2n6z7n"  # Replace with a strong value in production

    # Configure database
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://shiftlogix_user:AdminPassword1234@localhost/shiftlogix"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Configure JWT authentication and cookies
    app.config["JWT_SECRET_KEY"] = "age0ijl6uc0wve2n6z7n"  # Change this in production
    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # Disable for dev; enable in production
    app.config["JWT_COOKIE_SECURE"] = False  # Set to True in production with HTTPS
    app.config["JWT_COOKIE_SAMESITE"] = "Lax"

    # Initialize extensions
    if not app.extensions.get("sqlalchemy"):
        db.init_app(app)
    else:
        print("SQLAlchemy already initialized for this app")
    jwt.init_app(app)
    Migrate(app, db)

    with app.app_context():
        db.create_all()

    # Import and register Blueprints
    from backend.app.routes.authentication import auth_bp
    from backend.app.routes.home import home_bp
    from backend.app.routes.clock import clock_bp
    from backend.app.routes.schedule import schedule_bp
    from backend.app.routes.availability import availability_bp
    from backend.app.routes.employee_dashboard import employee_dashboard_bp
    from backend.app.routes.register import register_bp

    app.register_blueprint(clock_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(availability_bp)
    app.register_blueprint(employee_dashboard_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(home_bp)

    return app
