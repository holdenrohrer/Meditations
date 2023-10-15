import mysql.connector
from dotenv import load_dotenv
import os
from data import readIn

load_dotenv()

HOST = os.getenv("MYSQL_HOST")
DATABASE = os.getenv("MYSQL_DATABASE")
USER = os.getenv("MYSQL_USER")
PASSWORD = os.getenv("MYSQL_PASSWORD")

db = mysql.connector.connect(
    host=HOST, 
    database=DATABASE, 
    user=USER, 
    password=PASSWORD)

cursor = db.cursor()
db.commit()

