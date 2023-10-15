from flask import Flask
from data import *
from datetime import date

app = Flask(__name__);

"""
Enters Annotation Into Database
"""
def postAnnotation(token, sectionID, bookID, locationStart, locationEnd, text):
    data.addAnnotation(token, sectionID, bookID, locationStart, locationEnd, text)

"""
Enters Reflection Into Database
"""
def postReflection(token, bookID, sectionID, text):
    data.addReflection(token, bookID, sectionID, text)

"""
Getter
Returns Todays Reading as JSON
"""
@app.route('/todaysReading/<token>/', methods=['GET'])
def getTodaysReading(token):
    userJSON = data.getUser(token)
    today = str(date.today())
    if today == userJSON["last_day"]:
        sectionJSON = data.getSection(userJSON["book_id"], userJSON["section_id"])
        sectionJSON = data.getSection(userJSON["book_id"], userJSON["section_id"])
    else:
        data.setUser(None, None, None, today)
        sectionJSON = data.getSection(userJSON["book_id"], userJSON["section_id"])
        if data.checkLast(userJSON["book_id"], userJSON["section_id"]):
            sectionJSON["section_id"] = 0
        else:
            sectionJSON["section_id"] = sectionJSON["section_id"] + 1
    section = str(sectionJSON["section_id"])
    return sectionJSON
""" 
Getter
Returns Section Text as JSON
"""
@app.route('/section/<bookID>/<sectionID>', methods=['GET'])
def getSection(bookID, sectionID):
    return data.getSection(bookID, sectionID)

"""
Getter
Returns Annotation as JSON
"""
@app.route('/annotations/<token>/<bookID>/sectionID', methods=['GET'])
def getAnnotations(token, bookID, sectionID):
    return data.getAnnotation(token, bookID, sectionID)

app.run()

