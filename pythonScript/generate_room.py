from database_connection import get_connection
from faker import Faker
import random


faker = Faker()

conn = get_connection()
cursor = conn.cursor()

room_types = ['Single', 'Double', 'ICU', 'Deluxe']
status_choices = ['Available', 'Occupied', 'Maintenance']
total_rooms = 200
room_data = []

# Generate 200 unique room numbers (e.g., R001 to R200)
for i in range(1, total_rooms + 1):
    room_number = f"R{i:03d}"
    room_type = random.choice(room_types)
    availability_status = random.choices(
        status_choices, weights=[0.3, 0.6, 0.1], k=1
    )[0]  # e.g., more rooms are occupied

    assigned_patient_id = None
    if availability_status == 'Occupied':
        assigned_patient_id = random.randint(1, 3_000_000)

    department_id = random.randint(1, 15)

    room_data.append((
        room_number,
        room_type,
        availability_status,
        assigned_patient_id,
        department_id
    ))

cursor.executemany("""
    INSERT INTO Room (
        room_number, room_type, availability_status,
        assigned_patient_id, department_id
    )
    VALUES (%s, %s, %s, %s, %s)
""", room_data)

conn.commit()
cursor.close()
conn.close()

print("Successfully inserted 200 room records.")

