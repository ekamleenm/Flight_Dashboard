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
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            cursor = conn.cursor()

        except Error as e:
            print(f"Error: {e}")


    def fetch_city_names(self):
        pass