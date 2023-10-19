from tkinter import *
from tkcalendar import Calendar
from tkinter.font import Font
from tkinter import messagebox
import datetime
import json
from time import sleep
from utils import backend


def no_close():
    messagebox.showerror("Failed", "The window cannot be closed")


class DatePicker(Tk):
    def __init__(self, back_func):
        status = backend.checkStatus()
        super().__init__()
        self.font = Font(size=15)
        self.title("User Login")
        self.protocol("WM_DELETE_WINDOW", no_close)
        self.focus_force()
        self.attributes('-topmost', True)

        Label(self, text="Select date of the Wedding",
              anchor='center', font=self.font).grid()
        self.cal = Calendar(
            self, selectmode='day', date_pattern='y-mm-dd', mindate=datetime.date.today())
        self.cal.grid()

        Button(self, text="Enter", command=self.func,
               font=self.font, width=5).grid(column=0, row=2)
        Button(self, text="Back", font=self.font, width=5, command=lambda: [
               self.destroy(), back_func(status)]).grid(column=1, row=2)

    def func(self):
        if self.cal.get_date() != "":
            with open("data/temp.json", "r") as f:
                TempData = json.load(f)
            TempData['date'] = self.cal.get_date()
            with open("data/temp.json", "w") as f:
                json.dump(TempData, f, indent=4)

            self.destroy()
            print(f"You selected {self.cal.get_date()}")
            sleep(3)
        else:
            messagebox.showerror("Failed", "Please select a date.")
