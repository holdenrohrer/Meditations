from app import *
from data import *
from flask import Flask

def main():
    data.readIn(data, "test_book.txt", "Meditations", "Marcus Aurelius", 1, 1)

def todays_reading():
    returnJson = app.getTodaysReading("John")
    print(str(returnJson))

def getSection():
    sectionData = data.getSection(data, 1)
    print(sectionData)

def addReflection():
    data.addReflection(data, 1, "John", "I really like the emphasis on Meditation", 1)

addReflection()