from database_connection import get_connection;
from faker import Faker;
from random import choice;
from tqdm import tqdm;

faker = Faker();
genders = ['Male', 'Female', 'Other'];

conn = get_connection();
cursor = conn.cursor();

# batch insert into the patient table
BATCH_SIZE = 60000;
TOTAL_RECORD = 3_000_000;

for _ in tqdm(range(TOTAL_RECORD // BATCH_SIZE)):
    data = [];
    for _ in range(BATCH_SIZE):
        first_name = faker.first_name();
        last_name = faker.last_name();
        gender = choice(genders);
        dob = faker.date_of_birth(minimum_age=0, maximum_age=100).strftime('%Y-%m-%d');
        email = faker.unique.email();
        address = faker.address().replace('\n', ', ');
        phone = '0' + ''.join(faker.random_choices(elements='123456789', length=8))  # e.g. '0961234567'
        emergency_contact = faker.name();
        emergency_contact_phone = '0' + ''.join(faker.random_choices(elements='123456789', length=8))  # e.g. '0961234567'
        registration_date = faker.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')
        
        data.append((
            first_name,
            last_name,
            gender,
            dob,
            email,
            address,
            phone,
            emergency_contact,
            emergency_contact_phone,
            registration_date
        ));
    
    insert_query = """
        INSERT INTO Patient (first_name, last_name, gender, dob, email, address, phone, emergency_contact, emergency_contact_phone, registration_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, data);
    conn.commit();

# Close the cursor and connection
cursor.close();
conn.close();

print("Patient table populated successfully with 3,000,000 records.")