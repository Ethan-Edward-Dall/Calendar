# Ethan Dall
# May 16th, 2021
# calendarGUI.py

'''Imports'''
import datetime
import calendar
from tkinter import *
import tkinter

'''Date Class'''
# This class is to get/set the date month, day, year, and objects
class Date:

    def __init__(self):
        current = datetime.datetime.now()
        dateList = [current.day, current.month, current.year]
        self.setDate(str(dateList[0]), str(dateList[1]), str(dateList[2]))

    # This constructor is for the date object
    def setDate(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    # This method will set the day variable
    def setDay(self, day):
        self.day = day
    
    # This method will set the month variable
    def setMonth(self, month):
        self.month = month

    # This method will set the year variable
    def setYear(self, year):
        self.year = year
        

'''GUI Class'''
# This is initialized as a class to achieve the following:
# - Create static GUI layouts for proper visualization
# - Adapt to new features that can be added into the initialization process
class GUI(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        master.title("Busy Calendar")
        #master.geometry("500x500")

        masterFrame = Frame(self.master)
        self.create_widgets(masterFrame)

    # Create a grid that is 10x9, this will leave room for future additions
    def create_widgets(self, con):

        # Month and Year Labels
        date = Date()

        self.titleFrame = Frame(self.master)
        self.titleFrame.grid(column=0, row=0, padx=10, pady=10)
        self.setTitle(self.titleFrame, date)
        
        self.btnFrame = Frame(self.master)
        self.btnFrame.grid(column=0, row=1, padx=10, pady=10)
        self.genButtons(self.btnFrame, date)

    # This method will set and display the current month and year
    def setTitle(self, frame, date):
        MONTH_DICT = {"1":"January", "2":"Feburary", "3":"March", "4":"April", "5":"May", "6":"June",
         "7":"July", "8":"August", "9":"September", "10":"October", "11":"November", "12":"December"}

        # Buttons to change Month and Year
        self.subMonthBtn = Button(self.titleFrame, text="<", command= lambda: self.subMonth(date)).grid(row=0, column=1, pady=5, sticky=W)
        self.addbMonthBtn = Button(self.titleFrame, text=">", command= lambda: self.addMonth(date)).grid(row=0, column=7, pady=5, sticky=E)
        
        self.month = Label(frame, fg="blue", text=MONTH_DICT[date.month], font=("Arial", 25))
        self.month.grid(row=0, column=2, columnspan=5, pady=5, sticky=S)
        self.year = Label(frame, text=date.year)
        self.year.grid(row=1, column=2, columnspan=5, pady=5, sticky=N)

    # This method will generate the day buttons
    def genButtons(self, frame, date):
        MONTHLENGTH_DICT = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        # Day-of-the-week Labels
        self.mondayLabel = Label(frame, text="Mon")
        self.mondayLabel.grid(row=0, column=1, pady=5)
        self.teusdayLabel = Label(frame, text="Teu")
        self.teusdayLabel.grid(row=0, column=2, pady=5)
        self.wedLabel = Label(frame, text="Wed")
        self.wedLabel.grid(row=0, column=3, pady=5)
        self.thursdayLabel = Label(frame, text="Thur")
        self.thursdayLabel.grid(row=0, column=4, pady=5)
        self.fridayLabel = Label(frame, text="Fri")
        self.fridayLabel.grid(row=0, column=5, pady=5)
        self.saturdayLabel = Label(frame, fg="blue", text="Sat")
        self.saturdayLabel.grid(row=0, column=6, pady=5)
        self.sundayLabel = Label(frame, fg="blue", text="Sun")
        self.sundayLabel.grid(row=0, column=7, pady=5)

        # Date Button Layout, Manually input the first and last week-layout 
        weekDay = calendar.weekday(int(date.year), int(date.month), 1)
        stepper = 1
        dayNum = 1

        # First Week
        add = MONTHLENGTH_DICT[int(date.month)-1]
        for row in range(1):
            for col in range(7):
                if(col >= weekDay):
                    Button(frame, text=dayNum, command=self.execute).grid(row=1, column=col+1, padx=5, pady=5)
                    dayNum+=1
                    stepper+=1
                else:
                    Button(frame, fg="grey", text=(add-weekDay+1), command=self.execute).grid(row=1, column=col+1, padx=5, pady=5)
                    add+=1
                    stepper+=1
        
        # Weeks second through fourth
        for i in range(3):
            for j in range(7):
                self.gridButtons = Button(frame, text=dayNum, command=self.execute).grid(row=i+2, column=j+1, padx=5, pady=5)
                dayNum+=1
                stepper+=1

        # Fifth Week
        add = 1
        for k in range(1):
            for l in range(7):
                if(l+21+(7-weekDay) < MONTHLENGTH_DICT[int(date.month)]):
                    Button(frame, text=dayNum, command=self.execute).grid(row=5, column=l+1, padx=5, pady=5)
                    dayNum+=1
                else:
                    Button(frame, fg="grey", text=add, command=self.execute).grid(row=5, column=l+1, padx=5, pady=5)
                    add+=1

        # Possible Sixth Week
        for n in range(1):
            for m in range(7):
                if(dayNum <= MONTHLENGTH_DICT[int(date.month)]):
                    Button(frame, text=dayNum, command=self.execute).grid(row=6, column=m+1, padx=5, pady=5)
                    dayNum+=1
                else:
                    Button(frame, fg="grey", text=add, command=self.execute).grid(row=6, column=m+1, padx=5, pady=5)
                    add+=1
                


    # This method will take the user back one month
    def subMonth(self, date):
        # Get the current date, then check if its in Jan or 1970
        month = date.month
        year = date.year
        if(month != "1"):
            newMonth = int(month)-1
            newMonth = str(newMonth)
            # Delete generated Buttons within the btnFrame
            self.titleFrame.destroy()
            self.btnFrame.destroy()

            # Recreate title and month generation
            self.titleFrame = Frame(self.master)
            self.titleFrame.grid(column=0, row=0, padx=10, pady=10)
            self.btnFrame = Frame(self.master)
            self.btnFrame.grid(column=0, row=1, padx=10, pady=10)
            date.setMonth(newMonth)
            print(date.day, date.month, date.year)
            self.setTitle(self.titleFrame, date)
            self.genButtons(self.btnFrame, date)

        else:
            if(year == "1970"):
                print("Min date achieved")
            else:
                year = str(int(year)-1)
                month = "12"
                # Delete generated Buttons within the btnFrame
                self.btnFrame.destroy()
                self.titleFrame.destroy()

                # Recreate title and month generation
                self.titleFrame = Frame(self.master)
                self.titleFrame.grid(column=0, row=0, padx=10, pady=10)
                self.btnFrame = Frame(self.master)
                self.btnFrame.grid(column=0, row=1, padx=10, pady=10)
                date.setMonth(month)
                date.setYear(year)
                self.setTitle(self.titleFrame, date)
                self.genButtons(self.btnFrame, date)


    # This method will take the user back one month
    def addMonth(self, date):
        # Get the current date, then check if its in Jan or 1970
        month = date.month
        year = date.year
        if(month != "12"):
            month = int(month)+1
            newMonth = str(month)
            # Delete generated Buttons within the btnFrame
            self.titleFrame.destroy()
            self.btnFrame.destroy()

            # Recreate title and month generation
            self.titleFrame = Frame(self.master)
            self.titleFrame.grid(column=0, row=0, padx=10, pady=10)
            self.btnFrame = Frame(self.master)
            self.btnFrame.grid(column=0, row=1, padx=10, pady=10)
            date.setMonth(newMonth)
            print(date.day, date.month, date.year)
            self.setTitle(self.titleFrame, date)
            self.genButtons(self.btnFrame, date)

        else:
            year = str(int(year)+1)
            month = "1"
            # Delete generated Buttons within the btnFrame
            self.btnFrame.destroy()
            self.titleFrame.destroy()

            # Recreate title and month generation
            self.titleFrame = Frame(self.master)
            self.titleFrame.grid(column=0, row=0, padx=10, pady=10)
            self.btnFrame = Frame(self.master)
            self.btnFrame.grid(column=0, row=1, padx=10, pady=10)
            date.setMonth(month)
            date.setYear(year)
            self.setTitle(self.titleFrame, date)
            self.genButtons(self.btnFrame, date)
    
    def execute(self):
        print("Successful")

    # This method will change the size of the GUI window
    def changeSize(self, size):
        self.master.geometry(size)

    # This method will change the title of the GUI window
    def changeTitle(self, title):
        self.master.title(title)

# The final step to showing the generated GUI, giving it a root and application frame
root = tkinter.Tk()
app = GUI(root)
app.mainloop()
