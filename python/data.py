import json
import mysql.connector
from dotenv import load_dotenv
import os

class data:
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

    def __init__(self):
        self.cursor = self.db.cursor()

    def getUser(self, user_id):
        query = "SELECT user_name, last_day, section_id from user where user_id = %s"
        name = "Anonymous"
        self.cursor.execute(query, (user_id, ))
        for (user_name, last_day, section_id) in self.cursor:
            name = user_name
            last = last_day
            section = section_id
        user_data = {"user_id": user_id,"user_name": name, "last_day": last, "section_id": section}
        return user_data

    def getSection(self, sectionID):
        query = "SELECT section_id, book_name, author, section_name, texts, next_section, last_date from section where section_id = %s"
        section_data = {}
        self.cursor.execute(query, (sectionID,))
        for (section_id, book_name, author, section_name, texts, next_section, last_date) in self.cursor:
            section_data = {"section_id": section_id, "book_name": book_name, "author": author, "section_name": section_name, "texts": texts, "next_section": next_section, "last_date": last_date}
        return section_data
    
    def setUser(self, user_id, date): 
        query = "UPDATE user SET last_day = %s where user_id = %s"
        self.cursor.execute(query,(date, user_id))
        self.db.commit()

    def getReflection_Section(self, sourceID):
        query = "SELECT reflections_id, texts, user_id from reflections where section_id = %s"
        reflections = []
        reflection_data = {}
        self.cursor.execute(query, (sourceID, ))
        for (reflections_id, texts, user_id) in self.cursor:
            reflection_data = {"reflections_id": reflections_id,"texts": texts, "user_id": user_id}
            reflections.append(reflection_data)
        return reflections
    
    def addReflection(self, sectionID, userID, text, reflectionsID):
        query = "Insert into reflections (section_id, user_id, texts, reflections_id) values (%s, %s, %s, %s)"
        self.cursor.execute(query, (sectionID, userID, text, reflectionsID))
        self.db.commit()

    """
    Read New Book Into Database
    """
    def readIn(self, file_name, text_name, author, bookID, startSectionID):
        toRead = open(file_name,"r")
        text = toRead.read()
        sections = text.split("!!!BREAK!!!")
        new_section_id = startSectionID
        display_number = 1
        for section in sections:
            query = "INSERT INTO section (section_id, book_name, author, section_name, texts, next_section, is_last, last_date) values (%s, %s, %s, %s, %s, %s, %s, %s)"
            section_name = "Section " + str(display_number)
            next_section = new_section_id + 1
            last = False
            if (section == sections[-1]):
                last = True
                next_section = startSectionID
            self.cursor.execute(query,(new_section_id, text_name, author, section_name, section, next_section, last, "2000-01-01"))
            self.db.commit()
            new_section_id = new_section_id + 1

    def checkLast(self, sectionID):
        query = "SELECT is_last from section where section_id = %s"
        self.cursor.execute(query,(sectionID))
        for (is_last) in self.cursor:
            return is_last
        return False