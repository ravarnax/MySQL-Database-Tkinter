
import pymysql

def initialize_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        autocommit=True
    )
    cursor = conn.cursor()
    create_database(cursor)
    cursor.execute("USE tutorial")  # <- This must be before create_table
    create_table(cursor)
    
    print("Using database: tutorial")
    cursor.execute("SHOW TABLES")
    print("Tables:", cursor.fetchall())

    return conn, cursor

 
def create_database(cursor):
    cursor.execute("SHOW DATABASES")
    databases = [item[0] for item in cursor.fetchall()]
    if "tutorial" not in databases:
        cursor.execute("CREATE DATABASE tutorial")

 
def create_table(cursor):  
    cursor.execute("SHOW TABLES")
    temp = cursor.fetchall()
    tables = [item[0] for item in temp]
     
    if "users" not in tables:
        cursor.execute("""CREATE TABLE users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            firstName VARCHAR(100),
            lastName VARCHAR(100),
            password VARCHAR(30),
            email VARCHAR(100) UNIQUE,
            gender VARCHAR(1),
            age INT,
            address VARCHAR(200)
         )""")
 
def login(cursor, data):
    cursor.execute(f"""SELECT * FROM users WHERE email = '{data["email"]}' 
                       AND password = '{data["password"]}' """)
     
    if cursor.fetchone() != None:
        return True
    return False
 
def register(cursor, conn, data):
    print(data)
 
    cursor.execute(f"""INSERT INTO users values( 
        NULL,
        '{data["firstName"]}', 
        '{data["lastName"]}', 
        '{data["password"]}', 
        '{data["email"]}', 
        '{data["gender"]}', 
        '{data["age"]}', 
        '{data["address"]}'
    )""")
 
    conn.commit()


def fetch_all_users(cursor):
    """Return every row from the users table"""
    cursor.execute(
        "SELECT id, firstName, lastName, email, gender, age, address FROM users ORDER BY id"
    )
    
    return cursor.fetchall()


def validate_current_password(cursor, email, current_password):
    cursor.execute(f"SELECT password FROM users WHERE email='{email}'")
    result = cursor.fetchone()
    return result and result[0] == current_password

def change_password(cursor, conn, email, new_password):
    cursor.execute(f"UPDATE users SET password = '{new_password}' WHERE email='{email}'")
    conn.commit()

