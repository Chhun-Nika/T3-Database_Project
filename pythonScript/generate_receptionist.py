from database_connection import get_connection
from faker import Faker
import random

faker = Faker()

conn = get_connection()

cursor = conn.cursor()

# Possible shift values
shifts = ['Morning', 'Evening', 'Night', 'Other']

receptionist_data = []

# 2 receptionists for each of 15 departments
for department_id in range(1, 16):
    for _ in range(2):
        first_name = faker.first_name()
        last_name = faker.last_name()
        phone = '0' + ''.join(faker.random_choices(elements='123456789', length=8))
        email = faker.unique.email()
        hire_date = faker.date_between(start_date='-5y', end_date='today')
        shift = random.choice(shifts)

        receptionist_data.append((
            first_name,
            last_name,
            phone,
            email,
            hire_date,
            shift,
            department_id
        ))

# Insert into the Receptionist table
cursor.executemany("""
    INSERT INTO Receptionist (
        first_name, last_name, phone, email, hire_date, shift, department_id
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
""", receptionist_data)

conn.commit()
print("Successfully inserted 30 receptionists.")

cursor.close()
conn.close()