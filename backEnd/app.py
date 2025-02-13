from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()  # Ensure PyMySQL is recognized

app = Flask(__name__)

# MySQL Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://shiftlogix_user:AdminPassword1234@localhost/shiftlogix"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
    return {"message": "ShiftLogix API is running w/ SQLAlchemy"}

if __name__ == "__main__":
    app.run(debug=True)

