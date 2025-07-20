import mysql.connector;

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nika@Ax99',
            database='hospital'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None