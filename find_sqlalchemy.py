import os

# Define the directory to search (Update this if your project is in a different location)
project_directory = "C:\\Users\\r2nea\\OneDrive\\NAU_Files\\CS-440\\Project_1\\main\\ShiftLogix"

# Loop through all Python files and search for "SQLAlchemy()"
for root, _, files in os.walk(project_directory):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                for line_number, line in enumerate(f, 1):
                    if "SQLAlchemy()" in line:
                        print(f"Found in {file_path} (Line {line_number}): {line.strip()}")
