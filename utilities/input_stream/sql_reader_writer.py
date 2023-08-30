import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host="localhost",
    user=os.environ.get("SQL_USER_NAME"),
    password=os.environ.get("SQL_PASSWORD")
)

print(db)
