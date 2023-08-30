import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host="localhost",
    user=os.environ.get("SQL_USER_NAME"),
    password=os.environ.get("SQL_PASSWORD"),
    database="calco_games_test"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM users")

result = cursor.fetchall()

for x in result:
    print(x)
