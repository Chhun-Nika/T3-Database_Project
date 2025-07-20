from database_connection import get_connection
from faker import Faker
from random import choice, randint
from tqdm import tqdm


faker = Faker()
# 15 department-specialization 
# since specialization of doctors is fixed to one of the 15 departments
department_specializations = {
    1: 'Cardiology',
    2: 'Neurology',
    3: 'Pediatrics',
    4: 'Oncology',
    5: 'Orthopedics',
    6: 'Dermatology',
    7: 'Radiology',
    8: 'Psychiatry',
    9: 'Anesthesiology',
    10: 'Gastroenterology',
    11: 'Endocrinology',
    12: 'Urology',
    13: 'Hematology',
    14: 'Nephrology',
    15: 'Pulmonology'
}
genders = ['Male', 'Female', 'Other'];

conn = get_connection()
cursor = conn.cursor()

# batch insert into the doctor table
doctor_data = []
for _ in tqdm(range(3000), desc="Inserting Doctors"):
    dep_id = choice(list(department_specializations.keys()))
    specialization = department_specializations[dep_id]
    first_name = faker.first_name()
    last_name = faker.last_name()
    gender = choice(genders)
    dob = faker.date_of_birth(minimum_age=25, maximum_age=65).strftime('%Y-%m-%d')
    phone = '0' + ''.join(faker.random_choices(elements='123456789', length=8))  # e.g. '0961234567'
    email = faker.unique.email()
    hire_date = faker.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d')
    doctor_data.append((
        dep_id,
        first_name,
        last_name,
        gender,
        dob,
        specialization,
        phone,
        email,
        hire_date
    ));



insert_query = """
    INSERT INTO Doctor (dep_id, first_name, last_name, gender, dob, specialization, phone, email, hire_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""



cursor.executemany(insert_query, doctor_data)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Doctor table populated successfully with 3000 doctors.")