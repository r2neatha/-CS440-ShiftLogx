from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://shiftlogix_user:AdminPassword1234@localhost/shiftlogix"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Ensure application context is pushed when running the app
app.app_context().push()

@app.route("/")
def home():
    return {"message": "ShiftLogix API is running with SQLAlchemy"}

if __name__ == "__main__":
    app.run(debug=True)
