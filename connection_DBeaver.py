import mysql.connector
from mysql.connector import Error


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
        city = []
        self.cursor.execute("""SELECT DISTINCT(Source) FROM flights_app.flights 
                               UNION SELECT DISTINCT (Destination) FROM flights_app.flights """)

        data = self.cursor.fetchall()
        for item in data:
            city.append(item[0])  # b/c fetchall returns row s as tuples. e.g. [(surrey,),(Langley,) ...]

        return city

    def fetch_all_flights(self, source, destination):
        self.cursor.execute(
            """SELECT Airline,Route,Dep_Time,Duration,Price FROM flights f WHERE Source = '{}' AND Destination ='{}'""".format(
                source, destination))
        data = self.cursor.fetchall()
        return data
