from faker import Faker
import random
from database_connection import get_connection
from tqdm import tqdm

faker = Faker()

NUM_PRESCRIPTIONS = 4_000_000

conn = get_connection()
cursor = conn.cursor()


data = []
BATCH_SIZE = 60000

for _ in tqdm(range(NUM_PRESCRIPTIONS), desc="Inserting Prescriptions"):
    medical_record_id = random.randint(1, 5_000_000)
    date_issued = faker.date_between(start_date='-2y', end_date='today')
    notes = faker.paragraph(nb_sentences=3)
    data.append((medical_record_id, date_issued, notes))

    if len(data) >= BATCH_SIZE:
        cursor.executemany("""
            INSERT INTO Prescription (medical_record_id, date_issued, notes)
            VALUES (%s, %s, %s)
        """, data)
        conn.commit()
        data = []

# Final leftover batch
if data:
    cursor.executemany("""
        INSERT INTO Prescription (medical_record_id, date_issued, notes)
        VALUES (%s, %s, %s)
    """, data)
    conn.commit()

cursor.close()
conn.close()

print ("Prescription table populated successfully with 4_000_000 records.")