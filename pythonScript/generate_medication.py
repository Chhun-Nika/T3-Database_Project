from database_connection import get_connection
from faker import Faker
import random

faker = Faker();

conn = get_connection();
cursor = conn.cursor();

medications = []
for _ in range(1000):
    name = faker.unique.lexify(text='Medicine ???')
    description = faker.sentence(nb_words=8)
    unit_price = round(random.uniform(1.00, 500.00), 2)
    expiration_date = faker.date_between(start_date='+1y', end_date='+3y').strftime('%Y-%m-%d')
    medications.append((
        name, 
        description,
        unit_price,
        expiration_date
    ))

insert_query = """
    INSERT INTO Medication (name, description, unit_price, expiration_date) 
    VALUES (%s, %s, %s, %s)
"""


cursor.executemany(insert_query, medications)
conn.commit()

cursor.close()
conn.close()

print("Medication table populated successfully with 1000 records.");

