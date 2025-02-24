``markdown
# ShiftLogix

ShiftLogix is a full-stack web application designed to manage employee scheduling, time tracking, and authentication. The project uses a Flask-based backend with MySQL as the database engine and a simple HTML/CSS frontend. This README provides instructions to set up your development environment, install dependencies, configure the database, and run the application.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Folder Structure](#folder-structure)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Contact](#contact)

## Features

- **Employee Authentication:** Login and registration with JWT token generation.
- **Shift Scheduling:** Manage employee shifts and view schedules.
- **Time Tracking:** Clock in/out functionality with timesheet management.
- **User Dashboard:** Role-based views and dashboards (future enhancements planned).

## Getting Started

Follow these steps to get your local development environment up and running.

### Prerequisites

- Python 3.x installed on your system
- MySQL server installed and running
- Git (optional, for version control)
- A terminal/command prompt

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/shiftlogix.git
   cd shiftlogix
   ```

2. **Set Up the Virtual Environment:**

   On Windows:
   ```bash
   cd ShiftLogix\backend
   venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   cd ShiftLogix/backend
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   After activating the virtual environment, install all required packages:
   ```bash
   pip install -r requirements.txt
   ```

   *Alternatively, install packages manually:*
   ```bash
   pip install flask flask-restful flask-sqlalchemy flask-migrate flask-jwt-extended pymysql cryptography flask-bcrypt requests
   ```

4. **Verify Installation:**

   Check that your virtual environment is active and dependencies are installed:
   ```bash
   pip list
   ```

## Folder Structure

The project is organized as follows:

```
ShiftLogix/
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── home.py           # Home page route: /
│   │   │   ├── authentication.py # Login endpoint: /login
│   │   │   └── clock.py          # Clock in/out endpoint: /clock
│   │   ├── validators/
│   │   │   ├── __init__.py
│   │   │   └── log_in_validator.py
│   │   ├── __init__.py           # Initializes Flask, DB, and registers blueprints
│   │   └── models.py             # Database models and helper functions
│   └── venv/                     # Virtual environment folder
├── frontend/
│   └── route_templates/
│       ├── Home.html
│       ├── Login.html
│       ├── Clock.html
│       └── (additional HTML templates)
├── scripts/
│   ├── reset_database.py         # (Optional) Reset the database
│   ├── add_sample_employee.py    # Populate with test employee data
│   └── add_sample_data.py        # Populate with full sample data
├── tests/                        # (Optional) Test files and scripts
└── run.py                        # Main entry point to run the application
```

## Database Setup

ShiftLogix uses a MySQL database. Follow these steps to configure your database:



## Running the Application

1. **Start the Flask Application:**

   Make sure your virtual environment is activated and then run:
   ```bash
   python run.py
   ```

2. **Test the Endpoints:**

   - Open a browser or use Postman to visit `http://localhost/ShiftLogix/` for the home page.
   - Test authentication at `http://localhost/ShiftLogix/login`.
   - Test clock in/out functionality at `http://localhost/ShiftLogix/clock`.

## Testing

To test login and other functionalities, use the provided test script:

1. **Start the Flask app (if not already running):**
   ```bash
   python backend/run.py
   ```

2. **Open a new terminal, activate the virtual environment, and run the login test script:**
   ```bash
   python scripts/log_in_test_script.py
   ```

## Technologies Used

- **Backend:** Flask, Flask-RESTful, Flask-SQLAlchemy, Flask-Migrate, Flask-JWT-Extended
- **Frontend:** HTML (templates located in `/frontend/route_templates`)
- **Database:** MySQL (using PyMySQL with SQLAlchemy ORM)
- **Additional Libraries:** Cryptography, Flask-Bcrypt, Requests
