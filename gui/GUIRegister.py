from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import utils


def no_close():
    messagebox.showerror("Failed", "The window cannot be closed")


class UserRegisterGUI(Tk):

    def __init__(self, back_func):
        super().__init__()
        self.font = Font(size=15)
        self.title("User Register")
        self.protocol("WM_DELETE_WINDOW", no_close)
        self.focus_force()
        self.attributes('-topmost', True)

        self.name = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.contact = StringVar()

        Label(self, text="Full Name", font=self.font).grid(
            row=1, pady=20, padx=10)
        Entry(self, textvariable=self.name, font=self.font).grid(
            row=1, column=1, padx=10)

        Label(self, text="Username", font=self.font).grid(
            row=2, pady=20, padx=10)
        Entry(self, textvariable=self.username, font=self.font).grid(
            row=2, column=1, padx=10)

        Label(self, text="Password", font=self.font).grid(
            row=3, pady=20, padx=10)
        Entry(self, textvariable=self.password, font=self.font).grid(
            row=3, column=1, padx=10)

        Label(self, text="E-Mail", font=self.font).grid(row=4, pady=20, padx=10)
        Entry(self, textvariable=self.email, font=self.font).grid(
            row=4, column=1, padx=10)

        Label(self, text="Contact", font=self.font).grid(
            row=5, pady=20, padx=10)
        Entry(self, textvariable=self.contact, font=self.font).grid(
            row=5, column=1, padx=10)

        Button(self, text="Enter", font=self.font, width=5,
               command=self.func).grid(row=6, column=0, pady=20, padx=10)
        Button(self, text="Back", font=self.font, width=5, command=lambda: [
               self.destroy(), back_func()]).grid(row=6, column=1)

    def func(self):
        if self.name.get() and self.username.get() and self.password.get() and self.email.get() and self.contact.get():
            if utils.backend.addUser(self.name.get(), self.username.get(), self.password.get(), self.email.get(), self.contact.get()):
                messagebox.showinfo("Registered", "Successfully registered")
                self.destroy()
                utils.helpers.userWelcome()
            else:
                messagebox.showerror("Failed", "Registration unsuccessful")
        else:
            messagebox.showerror("Missing Value", "Required value is missing")
