import mysql.connector as mysql
from tkinter import messagebox
from .. import exceptions
import pandas as pd
import json

with open("utils/config.json", "r") as f:
    config = json.load(f)

cnx = mysql.connect(user=config['mysql']['user'],
                    password=config['mysql']['password'],
                    database=config['mysql']['database'])
cnx.autocommit = True
cursor = cnx.cursor()


def deleteUser(username: str, password: str):
    cursor.reset()
    cursor.execute(
        "select username from user_data where username = %s", (username,))
    if (username,) in cursor:
        cursor.reset()
        cursor.execute(
            "select username, password from user_data where username = %s", (username,))
        if (username, password) in cursor:
            cursor.reset()
            cursor.execute(
                "delete from user_data where username = %s and password = %s", (username, password))
            return True
        else:
            messagebox.showerror(
                "Failed", "Username and Password do not match.")
            return False
    else:
        messagebox.showerror("Failed", "User does not exist.")
        return False


def deleteData(database):
    cursor.reset()
    print("Current Data :\n")
    print(pd.read_sql("select * from %s;" %
          (database,), cnx).to_string(index=False))

    sno = None
    while not sno:
        try:
            sno = int(input("Select SNo to delete : "))
            result = pd.read_sql(
                "select * from %s where sno = %s;" % (database, sno), cnx)
            if result.empty:
                raise exceptions.InvalidOption("Enter valid SNo.")
        except exceptions.InvalidOption as e:
            sno = None
            print(e)
        except ValueError:
            sno = None
            print("Enter valid SNo.")

    cursor.reset()
    try:
        pd.read_sql("delete from %s where sno = %s;" % (database, sno), cnx)
    except TypeError:
        pass
