import mysql.connector
from mysql.connector import Error
import streamlit


class DB:
    def __init__(self):
        host = 'localhost'
        user = 'root'
        password = ''
        database = 'flights_app'

        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            self.cursor = self.conn.cursor()

        except Error as e:
            print(f"Error: {e}")

    def fetch_city_names(self):
        self.cursor.execute("""SELECT DISTINCT(Source) FROM flights_app.flights UNION SELECT DISTINCT (Destination) FROM flights_app.flights """)
