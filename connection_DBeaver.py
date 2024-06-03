import mysql.connector
from mysql.connector import Error
import streamlit

# Database connection details
host = 'localhost'
user = 'root'
password = ''
database = 'flights_app'

try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE flights (
    Airline VARCHAR(255),
    Date_of_Journey DATE,
    Source VARCHAR(255),
    Destination VARCHAR(255),
    Route VARCHAR(255),
    Dep_Time TIME,
    Duration VARCHAR(255),
    Total_Stops VARCHAR(255),
    Price INT
)
""")


except Error as e:
    print(f"Error: {e}")

