from database_connection import get_connection
from faker import Faker
import random
from tqdm import tqdm

faker = Faker();

NUM_RECORDS =  5_000_000
APPOINTMENT_ID_RANGE = 6_000_000
BATCH_SIZE = 60_000
conn = get_connection();
cursor = conn.cursor()


# Generate 5 million unique appointment IDs from 1 to 6 million
appointment_ids = random.sample(range(1, APPOINTMENT_ID_RANGE + 1), k=NUM_RECORDS)
data = []
insert_query = """
    INSERT INTO Medical_Record (appointment_id, diagnosis, treatment, visit_date, notes)
    VALUES (%s, %s, %s, %s, %s)
"""
for i in tqdm(range(NUM_RECORDS), desc="Inserting Medical Records"):
    appointment_id = appointment_ids[i]
    diagnosis = faker.sentence(nb_words=6)
    treatment = faker.sentence(nb_words=8)
    visit_date = faker.date_between(start_date='-3y', end_date='today')
    notes = faker.paragraph(nb_sentences=2)

    data.append((appointment_id, diagnosis, treatment, visit_date, notes))

    # Insert in batches
    if len(data) == BATCH_SIZE:
        cursor.executemany(insert_query, data)
        conn.commit()
        data.clear()

# Insert any remaining records
if data:
    cursor.executemany(insert_query, data)
    conn.commit()

cursor.close()
conn.close()

print("Medical Record table populated successfully with 5_000_000 records.")

