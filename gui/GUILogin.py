import time
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import utils
import json

with open("utils/config.json", "r") as f:
    config = json.load(f)

def no_close():
    messagebox.showerror("Failed", "The window cannot be closed")


class UserLoginGUI(Tk):

    def __init__(self, back_func):
        super().__init__()
        self.font = Font(size=15)
        self.title("User Login")
        self.protocol("WM_DELETE_WINDOW", no_close)
        self.focus_force()
        self.attributes('-topmost', True)

        self.username = StringVar()
        self.password = StringVar()

        Label(self, text="Username", font=self.font).grid(
            row=1, column=0, pady=20, padx=10)
        Entry(self, font=self.font, textvariable=self.username).grid(
            row=1, column=1, padx=10)

        Label(self, text="Password", font=self.font).grid(
            row=2, column=0, padx=10)
        Entry(self, font=self.font, textvariable=self.password).grid(
            row=2, column=1, padx=10)

        Button(self, text="Enter", font=self.font, width=5,
               command=self.func).grid(row=3, column=0, pady=20, padx=10)
        Button(self, text="Back", font=self.font, width=5, command=lambda: [
               self.destroy(), back_func()]).grid(row=3, column=1, padx=10)

    def func(self):
        if utils.backend.checkUser(self.username.get(), self.password.get()):
            uData = utils.backend.selUserData(
                self.username.get(), self.password.get())
            self.destroy()
            with open("data/temp.json", "r") as f:
                TempData = json.load(f)
            TempData['sno'] = uData[0]
            TempData['name'] = uData[1]
            TempData['contact'] = uData[4]
            TempData['email'] = uData[5]

            with open("data/temp.json", "w") as f:
                json.dump(TempData, f, indent=4)

            utils.userLogger.initLogger()
        else:
            messagebox.showerror(title="Login failed",
                                 message="Username and Password do not match")


class UserDeleteGUI(Tk):

    def __init__(self, back_func):
        super().__init__()
        self.font = Font(size=15)
        self.title("Delete Account")
        self.protocol("WM_DELETE_WINDOW", no_close)
        self.focus_force()
        self.attributes('-topmost', True)

        self.username = StringVar()
        self.password = StringVar()

        Label(self, text="Username", font=self.font).grid(
            row=1, column=0, pady=20, padx=10)
        Entry(self, font=self.font, textvariable=self.username).grid(
            row=1, column=1, padx=10)

        Label(self, text="Password", font=self.font).grid(
            row=2, column=0, padx=10)
        Entry(self, font=self.font, textvariable=self.password).grid(
            row=2, column=1, padx=10)

        Button(self, text="Enter", font=self.font, width=5,
               command=self.func).grid(row=3, column=0, pady=20, padx=10)
        Button(self, text="Back", font=self.font, width=5, command=lambda: [
               self.destroy(), back_func()]).grid(row=3, column=1, padx=10)

    def func(self):
        if utils.backend.deleteUser(self.username.get(), self.password.get()):
            self.destroy()
            print("Successfully deleted")
            time.sleep(1)
            utils.helpers.userWelcome()


class AdminLoginGUI(Tk):

    def __init__(self, back_func):
        super().__init__()
        self.font = Font(size=15)
        self.title("Admin Login")
        self.protocol("WM_DELETE_WINDOW", no_close)
        self.focus_force()
        self.attributes('-topmost', True)

        self.username = StringVar()
        self.password = StringVar()

        Label(self, text="Username", font=self.font).grid(
            row=1, column=0, pady=20, padx=10)
        Entry(self, textvariable=self.username, font=self.font).grid(
            row=1, column=1, padx=10)

        Label(self, text="Password", font=self.font).grid(
            row=2, column=0, padx=10)
        Entry(self, textvariable=self.password, font=self.font).grid(
            row=2, column=1, padx=10)

        Button(self, text="Enter", font=self.font, width=5,
               command=self.func).grid(row=3, column=0, pady=20, padx=10)
        Button(self, text="Back", font=self.font, width=5, command=lambda: [
               self.destroy(), back_func()]).grid(row=3, column=1, padx=10)

    def func(self):
        if self.username.get() == config['admin']['username'] and self.password.get() == config['admin']['password']:
            self.destroy()
            utils.adminLogger.initLogger()
        else:
            messagebox.showerror(title="Login failed",
                                 message="Credentials do not match.")
