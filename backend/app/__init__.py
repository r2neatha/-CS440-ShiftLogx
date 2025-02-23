"""
File: ShiftLogix/backend/app/__init__.py
Purpose: Initializes the Flask application, database, and registers Blueprints.
"""

# Import necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager  # Import JWT for authentication

# Initialize Flask extensions
db = SQLAlchemy()
jwt = JWTManager()  # Initialize JWT

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)

    # Configure database
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://shiftlogix_user:AdminPassword1234@localhost/shiftlogix"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Configure JWT authentication
    app.config["JWT_SECRET_KEY"] = "your-secret-key"  # Change this in production

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)  # Bind JWT to Flask
    Migrate(app, db)

    with app.app_context():
        db.create_all()

    # Import and register Blueprints
    from backend.app.routes.authentication import auth_bp
    from backend.app.routes.home import home_bp  # Import home route
    
    # Add the following lines to register the clock blueprint:
    from backend.app.routes.clock import clock_bp
    app.register_blueprint(clock_bp)

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)  # Register the home page blueprint

    return app
