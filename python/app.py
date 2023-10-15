from flask import Flask
from data import *
from datetime import date

app = Flask(__name__);

"""
Getter
Returns Todays Reading as JSON
"""
@app.route('/todaysReading/<token>/', methods=['GET'])
def getTodaysReading(token):
    userJSON = data.getUser(data, token)
    today = str(date.today())
    if today == userJSON["last_day"]:
        sectionJSON = data.getSection(data, userJSON["section_id"])
    else:
        data.setUser(data, token, today)
        sectionJSON = data.getSection(data, userJSON["section_id"])
        if data.checkLast(data, userJSON["section_id"]):
            sectionJSON["section_id"] = 0
        else:
            sectionJSON["section_id"] = sectionJSON["next_section"]
    return sectionJSON
""" 
Getter
Returns Section Text as JSON
"""
@app.route('/section/<excerptID>', methods=['GET'])
def getSection(excerptID):
    return data.getSection(data, excerptID)

"""
Getter
Returns Annotation as JSON
"""
@app.route('/reflections_section/<sectionID>', methods=['GET'])
def getReflections(sectionID):
    return data.getReflection_Section(data, sectionID)

@app.route('/reflections_post/<sectionID>/<userID>/<text>/<reflectionsID>', methods=['POST'])
def postReflections(sectionID, userID, text, reflectionsID):
    data.addReflection(data, sectionID, userID, text, reflectionsID)


if __name__ == "__main__":
    app.run()