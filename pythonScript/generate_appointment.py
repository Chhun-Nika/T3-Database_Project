import random
from faker import Faker
from database_connection import get_connection
from tqdm import tqdm

faker = Faker()

status_options = ['Scheduled', 'Completed', 'Cancelled', 'No-Show']


conn = get_connection()
cursor = conn.cursor()

# SQL query
insert_query = """
    INSERT INTO Appointment (patient_id, doctor_id, appointment_datetime, reason, status)
    VALUES (%s, %s, %s, %s, %s)
"""

# Generate 6 million records
BATCH_SIZE = 60000
TOTAL_RECORD = 6_000_000

for _ in tqdm(range(TOTAL_RECORD // BATCH_SIZE), desc="Inserting Appointments"):
    data = []
    for _ in range(BATCH_SIZE):
        patient_id = random.randint(1, 3_000_000)
        doctor_id = random.randint(1, 3_000)
        appointment_datetime = faker.date_time_between(start_date='-3y', end_date='+1y').strftime('%Y-%m-%d %H:%M:%S')
        reason = faker.sentence(nb_words=6)
        status = random.choice(status_options)
        data.append ((
            patient_id,
            doctor_id,
            appointment_datetime,
            reason,
            status
        ));
    cursor.executemany(insert_query, data);
    conn.commit();

cursor.close();
conn.close();