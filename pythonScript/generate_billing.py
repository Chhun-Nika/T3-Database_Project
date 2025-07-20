from database_connection import get_connection
from faker import Faker
import random

faker = Faker()
conn = get_connection()
cursor = conn.cursor()

batch_size = 10000
offset = 0

# using offset to avoid story millions of data in list before inserting into database
while True:
    cursor.execute("""
        SELECT appointment_id, patient_id 
        FROM Appointment 
        LIMIT %s OFFSET %s
    """, (batch_size, offset))
    
    appointments = cursor.fetchall()
    if not appointments:
        break  # no more data

    billing_batch = []
    for appointment_id, patient_id in appointments:
        total_amount = round(random.uniform(20, 500), 2)
        payment_status = random.choice(['Pending', 'Paid', 'Cancelled'])
        billing_date = faker.date_between(start_date='-1y', end_date='today')
        payment_method = random.choice(['Cash', 'Credit Card', 'Insurance', 'Mobile Payment'])

        billing_batch.append((
            patient_id,
            appointment_id,
            total_amount,
            payment_status,
            billing_date,
            payment_method
        ))

    cursor.executemany("""
        INSERT INTO Billing (
            patient_id,
            appointment_id,
            total_amount,
            payment_status,
            billing_date,
            payment_method
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, billing_batch)
    
    conn.commit()
    offset += batch_size

cursor.close()
conn.close()
print("All billing records inserted successfully!")