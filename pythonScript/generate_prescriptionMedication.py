import random
from faker import Faker
from database_connection import get_connection
from tqdm import tqdm

faker = Faker()

BATCH_SIZE = 50000
TOTAL_PRESCRIPTIONS = 4_000_000
MAX_MEDICATIONS_PER_PRESCRIPTION = 3
TOTAL_MEDICATIONS = 1000

conn = get_connection()
cursor = conn.cursor()

insert_query = """
    INSERT INTO PrescriptionMedication (prescription_id, medication_id, dosage, frequency, duration)
    VALUES (%s, %s, %s, %s, %s)
"""

for batch_start in tqdm(range(0, TOTAL_PRESCRIPTIONS, BATCH_SIZE), desc="Inserting Prescription-Medication"):
    data = []
    for prescription_id in range(batch_start + 1, batch_start + BATCH_SIZE + 1):
        num_meds = random.randint(1, MAX_MEDICATIONS_PER_PRESCRIPTION)
        medication_ids = random.sample(range(1, TOTAL_MEDICATIONS + 1), num_meds)
        for med_id in medication_ids:
            dosage = f"{random.randint(1, 2)} tablets"
            frequency = random.choice(["Once a day", "Twice a day", "Every 8 hours"])
            duration = f"{random.randint(3, 14)} days"
            data.append((prescription_id, med_id, dosage, frequency, duration))
    cursor.executemany(insert_query, data)
    conn.commit()

cursor.close()
conn.close()

print("Prescription Medication table populated successfully")