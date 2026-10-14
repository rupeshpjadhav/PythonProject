"""Examples of saving and loading JSON objects, JSON arrays, and CSV rows."""

import csv
import json
from pathlib import Path


# Put generated example files beside this script, not in the terminal's folder.
EXAMPLE_FOLDER = Path(__file__).parent / "file_examples"
EXAMPLE_FOLDER.mkdir(exist_ok=True)
JSON_OBJECT_FILE = EXAMPLE_FOLDER / "person.json"
JSON_ARRAY_FILE = EXAMPLE_FOLDER / "students.json"
CSV_FILE = EXAMPLE_FOLDER / "students.csv"


# -----------------------------------------------------
# 1. JSON object: a Python dictionary saved as JSON
# -----------------------------------------------------
person = {
    "name": "Asha",
    "age": 25,
    "is_student": True,
    "skills": ["Python", "problem solving"],
    "address": {"city": "Pune", "country": "India"},
}

# json.dump writes Python data to an open file as JSON text.
with JSON_OBJECT_FILE.open("w", encoding="utf-8") as json_file:
    json.dump(person, json_file, indent=4)

# json.load reads JSON text from a file and converts it back to Python data.
with JSON_OBJECT_FILE.open("r", encoding="utf-8") as json_file:
    loaded_person = json.load(json_file)

print("--- JSON object / dictionary ---")
print("Name:", loaded_person["name"])
print("City:", loaded_person["address"]["city"])
print("Skills:", loaded_person["skills"])


# -----------------------------------------------------
# 2. JSON array: a Python list of objects
# -----------------------------------------------------
students = [
    {"id": 1, "name": "Asha", "marks": [88, 92, 95]},
    {"id": 2, "name": "Noah", "marks": [76, 84, 90]},
    {"id": 3, "name": "Mina", "marks": [91, 89, 94]},
]

# A list of dictionaries becomes a JSON array of JSON objects.
with JSON_ARRAY_FILE.open("w", encoding="utf-8") as json_file:
    json.dump(students, json_file, indent=4)

with JSON_ARRAY_FILE.open("r", encoding="utf-8") as json_file:
    loaded_students = json.load(json_file)

print("\n--- JSON array / list of dictionaries ---")
for student in loaded_students:
    average = sum(student["marks"]) / len(student["marks"])
    print(f"{student['name']}: average mark = {average:.1f}")


# json.dumps and json.loads work with JSON strings instead of files.
json_text = json.dumps(person, indent=2)
person_again = json.loads(json_text)
print("\nJSON string round-trip:", person_again["name"])


# -----------------------------------------------------
# 3. CSV: a table of rows and columns
# -----------------------------------------------------
csv_rows = [
    {"id": 1, "name": "Asha", "age": 25},
    {"id": 2, "name": "Noah", "age": 19},
    {"id": 3, "name": "Mina", "age": 22},
]
field_names = ["id", "name", "age"]

# newline="" is recommended for CSV files to avoid extra blank lines.
# DictWriter writes dictionaries using field_names as the column headers.
with CSV_FILE.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(csv_rows)

# DictReader uses the first row as column names and returns dictionaries.
with CSV_FILE.open("r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    loaded_rows = list(reader)

print("\n--- CSV rows ---")
for row in loaded_rows:
    # CSV values are read as strings; convert age if it is needed as a number.
    age = int(row["age"])
    print(f"{row['name']} is {age} years old.")


# -----------------------------------------------------
# 4. A basic CSV reader returns each row as a list
# -----------------------------------------------------
print("\n--- CSV using csv.reader ---")
with CSV_FILE.open("r", newline="", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    headings = next(reader)  # Read the header row separately.
    print("Columns:", headings)
    for row in reader:
        print("Row:", row)


# The examples create these files in concepts/file_examples/:
# - person.json: one JSON object (a dictionary)
# - students.json: a JSON array (a list of dictionaries)
# - students.csv: tabular rows with a header row
