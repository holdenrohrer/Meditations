import mysql.connector
from dotenv import load_dotenv
import os
from data import *

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

data.readIn(data, "Meditations.txt", "Meditations", "Marcus Aurelius", 1, 1)
cursor = db.cursor()
query = "Insert into user (user_id, user_name, section_id, last_day) values (%s, %s, %s, %s)"
cursor.execute(query, ("John", "John", 1, "2000-20-21"))
query = "Insert into user (user_id, user_name, section_id, last_day) values (%s, %s, %s, %s)"
cursor.execute(query, ("Mary", "Mary", 3, "2000-20-21"))
db.commit()
data.addReflection(data, 1, "John", "I really like the emphasis on Meditation", 1)
data.addReflection(data, 1, "Mary", "The langauge in this is so expressive.", 2)
data.addReflection(data, 1, "John", "Does anyone have any thoughts on line VI? I can't quite determine his meaning", 3)