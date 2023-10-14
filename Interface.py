"""
Enters Annotation Into Database
"""
def postAnnotation(token, sectionID, bookID, locationStart, locationEnd, text):
    print("postAnnotation")

"""
Enters Reflection Into Database
"""
def postReflection(token, bookID, sectionID, text):
    print("postReflection")

"""
Getter
Returns Todays Reading as JSON
"""
def getTodaysReading(token):
    print("getTodaysReflection")

"""
Getter
Returns Section Text as JSON
"""
def getSection(bookID, sectionID):
    print("getSection")

"""
Getter
Returns Annotation as JSON
"""
def getAnnotation(token, bookID, sectionID):
    print("getAnnotation")
"""
Read New Book Into Database
"""
def readIn(name):
    toRead = open(name,"r")
    text = toRead.read()