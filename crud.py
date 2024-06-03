import mysql.connector
from mysql.connector import Error

# Connect to the database server
try:
    my_conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='flight_dashboard'
    )
except Error as e:
    print(f"Error: {e}")

cursor = my_conn.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS flight_dashboard")
# conn.commit()

# Create Tables
cursor.execute("""CREATE TABLE IF NOT EXISTS airport (
                   airport_id INTEGER PRIMARY KEY,
                   code VARCHAR(10) NOT NULL,
                   city VARCHAR(50) NOT NULL,
                   name VARCHAR(255) NOT NULL)""")

#  When we perform write operation
my_conn.commit()

# cursor.execute("""INSERT INTO airport VALUES (1,'DEL','New Delhi','IGIA'),
#                                               (2,'CCU','Kolkata','NSCA'),
#                                               (3, 'BOM', 'Mumbai','CSMA')""")
# my_conn.commit()
# cursor.execute("""INSERT INTO airport VALUES (4, 'BOM', 'Mumbai','CSMA')""")
# my_conn.commit()

cursor.execute("""SELECT * FROM airport WHERE airport_id > 1 """)
data = cursor.fetchall()
print(data)



# UPDATE

cursor.execute("""UPDATE airport
                  SET city = 'Bombay'
                  WHERE airport_id = 4""")
my_conn.commit()

# cursor.execute("""DELETE FROM airport WHERE airport_id = 3""")
# my_conn.commit()

cursor.execute("""SELECT * FROM airport WHERE airport_id > 0 """)
data = cursor.fetchall()
print(data)
