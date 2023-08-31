import mysql.connector
import os
from dotenv import load_dotenv


class SQLReaderWriter:

    @staticmethod
    def db_connector(func):
        def with_connection(*args, **kwargs):
            load_dotenv()

            conn = mysql.connector.connect(
                host="localhost",
                user=os.environ.get("SQL_USER_NAME"),
                password=os.environ.get("SQL_PASSWORD"),
                database="calco_games_test"
            )

            try:
                result = func(*args, connection=conn, **kwargs)
            except:
                conn.rollback()
                print("SQL Failed")
                raise
            else:
                conn.connect()
            finally:
                conn.close()
            return result
        return with_connection

    @staticmethod
    def create():
        pass

    @staticmethod
    @db_connector
    def retrieve(query, *args, **kwargs):
        conn: mysql.connector.MySQLConnection = kwargs.pop("connection")

        cursor: mysql.connector.MySQLConnection.cursor = conn.cursor()

        cursor.execute(query)

        result = cursor.fetchall()

        return result
