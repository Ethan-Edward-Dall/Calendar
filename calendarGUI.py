# Ethan Dall
# May 16th, 2021
# calendarGUI.py

'''Imports'''
import datetime
import calendar
from tkinter import *

'''Date Class'''
# This class is to get/set the date month, day, year, and objects
class Date:
    day, month = "01"
    year = "0001"

    # This constructor is for the date object
    def Date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # This method will return the day variable
    def getDay(self):
        return self.day
    
    # This method will set the day variable
    def setDay(self, day):
        self.day = day

    # This method will return the month variable
    def getMonth(self):
        return self.month
    
    # This method will set the month variable
    def setMonth(self, month):
        self.month = month

    # This method will return the year variable
    def getYear(self):
        return self.year

    # This method will set the year variable
    def setYear(self, year):
        self.year = year

    # This method will return a list [DD, MM, YYYY]
    def getTodaysDate():
        current = datetime.datetime.now()
        dateList = [current.day, current.month, current.year]
        return dateList

    # This method will set the current date using the three attributes
    def setCurrentDate(self):
        self.day = getDay()
        self.month = getMonth()
        self.year = getYear()
        

'''GUI Class'''
# This is initialized as a class to achieve the following:
# - Create static GUI layouts for proper visualization
# - Adapt to new features that can be added into the initialization process
class GUI:
    def __init__(self, name, size):
        self.name = name
        self.size = size
