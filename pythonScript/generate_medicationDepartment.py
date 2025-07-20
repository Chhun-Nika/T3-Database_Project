import random
from database_connection import get_connection
from tqdm import tqdm


conn = get_connection();
cursor = conn.cursor();

# Constants
NUM_DEPARTMENTS = 15
NUM_MEDICATIONS = 1000

data = []

for medication_id in tqdm(range(1, NUM_MEDICATIONS + 1), desc="Linking Medications to Departments"):
    # Randomly choose 1 to 3 departments for this medication
    department_ids = random.sample(range(1, NUM_DEPARTMENTS + 1), k=random.randint(1, 3))
    for dept_id in department_ids:
        stock_quantity = random.randint(1, 500)  # random stock quantity
        data.append((dept_id, medication_id, stock_quantity))


# Prepare insert
insert_query = """
    INSERT INTO DepartmentMedication (department_id, medication_id, stock_quantity)
    VALUES (%s, %s, %s)
"""
# Insert all data
cursor.executemany(insert_query, data)
conn.commit()
cursor.close()
conn.close()

print("DepartmentMedication table populated successfully!")