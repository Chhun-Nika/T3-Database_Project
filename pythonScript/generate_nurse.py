from database_connection import get_connection
from faker import Faker
from random import choice
import random
from tqdm import tqdm


faker = Faker()
# Possible options
genders = ['Male', 'Female', 'Other']
shifts = ['Morning', 'Evening', 'Night', 'Other']

conn = get_connection()
cursor = conn.cursor()

# generate data for 6000 nureses
nurse_data = []
for _ in tqdm(range(6000), desc="Inserting Nurses"):
    first_name = faker.first_name()
    last_name = faker.last_name()
    gender = choice(genders)
    dob = faker.date_of_birth(minimum_age=22, maximum_age=60).strftime('%Y-%m-%d')
    dep_id = random.randint(1, 15)
    phone = '0' + ''.join(faker.random_choices(elements='123456789', length=8))  # e.g. '0961234567
    email = faker.unique.email()
    shift = choice(shifts)
    hire_date = faker.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d')

    nurse_data.append((
        first_name,
        last_name,
        gender,
        dob,
        dep_id,
        shift,
        phone,
        hire_date,
        email
    ))

insert_query = """
    INSERT INTO Nurse (first_name, last_name, gender, dob, dep_id, shift, phone, hire_date, email)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
cursor.executemany(insert_query, nurse_data)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Nurse table populated successfully with 6000 records.")

