from faker import Faker
import random
from database_connection import get_connection


faker = Faker()

department_specializations = [
    ("Cardiology", "Medical"),
    ("Neurology", "Medical"),
    ("Pediatrics", "Medical"),
    ("Oncology", "Medical"),
    ("Orthopedics", "Surgical"),
    ("Dermatology", "Medical"),
    ("Radiology", "Diagnostic"),
    ("Psychiatry", "Mental Health"),
    ("Anesthesiology", "Critical Care"),
    ("Gastroenterology", "Medical"),
    ("Endocrinology", "Medical"),
    ("Urology", "Surgical"),
    ("Hematology", "Medical"),
    ("Nephrology", "Medical"),
    ("Pulmonology", "Medical")
]

conn = get_connection()
cursor = conn.cursor()

# Randomly select 15 unique doctor IDs from range 1 to 3000
head_doctor_ids = random.sample(range(1, 3001), 15)
departments = []
for i, (name, dept_type) in enumerate(department_specializations):
    head_id = head_doctor_ids[i]

    # Generate building and floor (e.g., "Building B, Floor 3")
    building = f"Building {random.choice(['A', 'B', 'C', 'D', 'E'])}"
    floor = f"Floor {random.randint(1, 5)}"
    location = f"{building}, {floor}"

    departments.append((name, dept_type, head_id, location))
    
insert_query = """
    INSERT INTO Department (name, department_type, head_of_dep, location)
    VALUES (%s, %s, %s, %s)
"""
cursor.executemany(insert_query, departments)

conn.commit()
# Close the cursor and connection
cursor.close()
conn.close()

print("Department table populated successfully with head doctors and locations.")
