import mysql.connector as mysql
from tkinter import messagebox
import json
import pandas as pd
from .. import exceptions
import json

with open("utils/config.json", "r") as f:
    config = json.load(f)

cnx = mysql.connect(user=config['mysql']['user'],
                    password=config['mysql']['password'],
                    database=config['mysql']['database'])
cnx.autocommit = True
cursor = cnx.cursor()


def addUser(name: str, username: str, password: str, email: str, contact: str):
    cursor.reset()
    try:
        cursor.execute("insert into user_data (name, e_mail, contact, password, username) values (%s, %s, %s, %s, %s)",
                       (name, email, contact, password, username))
        return True
    except mysql.errors.IntegrityError:
        messagebox.showerror(
            "Used username", "Username has already been taken")
        return False
    except mysql.errors.DatabaseError:
        messagebox.showerror("Invalid Value", "Contact needs to be numeric")
        return False


def addFeedback(stars, feedback):
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    cursor.reset()
    cursor.execute("insert into feedbacks values (%s, %s, %s)",
                   (TempData['name'], stars, feedback))


def addVenue():
    print("Current data in Venues :\n")
    venues = pd.read_sql("select * from venue;", cnx).to_string(index=False)
    print(venues)
    cursor.reset()

    name = None
    while not name:
        name = input("Enter Name : ")
        if name == "":
            print("Name cannot be empty")
            name = None

    city = None
    while not city:
        city = input("Enter City : ")
        if city == "":
            print("City cannot be empty.")
            city = None

    address = None
    while not address:
        address = input("Enter Address : ")
        if address == "":
            print("Address cannot be empty")
            address = None

    vtype = None
    while not vtype:
        vtype = input("Enter Type : ")
        if vtype == "":
            print("Type cannot be empty")
            vtype = None

    rating = None
    while not rating:
        try:
            rating = int(input("Enter Rating : "))
            if rating not in [1, 2, 3, 4, 5]:
                raise exceptions.InvalidOption(
                    "Enter valid rating [1/2/3/4/5]")
        except exceptions.InvalidOption as e:
            rating = 0
            print(e)
        except ValueError:
            print("Enter valid rating [1/2/3/4/5]")

    size = None
    while not size:
        size = input("Enter Size : ")
        if size == "":
            print("Size cannot be empty")
            size = None

    availability = None
    while not availability:
        try:
            availability = int(input("Enter Availability : "))
            if availability not in [1, 0]:
                raise exceptions.InvalidOption(
                    "Enter valid availability [1/2]")
        except exceptions.InvalidOption as e:
            availability = None
            print(e)
        except ValueError:
            print("Enter valid availability [1/2]")

    ppp = None
    while not ppp:
        try:
            ppp = int(input("Enter Price per Plate : "))
        except ValueError:
            print("Enter valid Price per Plate.")

    cost = None
    while not cost:
        try:
            cost = int(input("Enter Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("insert into venue (name, city, address, type, rating, size, availability, price_per_plate, cost) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (name, city, address, vtype, rating, size, availability, ppp, cost))


def addCaterer():
    print("Current data in Caterers :\n")
    caterers = pd.read_sql("select * from catering;",
                           cnx).to_string(index=False)
    print(caterers)
    cursor.reset()

    name = None
    while not name:
        name = input("Enter Name : ")
        if name == "":
            print("Name cannot be empty")
            name = None

    city = None
    while not city:
        city = input("Enter City : ")
        if city == "":
            print("City cannot be empty.")
            city = None

    contact = None
    while not contact:
        try:
            contact = int(input("Enter Contact : "))
        except ValueError:
            print("Enter valid Contact")

    details = None
    while not details:
        details = input("Enter Details : ")
        if details == "":
            print("Details cannot be empty.")
            details = None

    availability = None
    while not availability:
        try:
            availability = int(input("Enter Availability : "))
            if availability not in [1, 0]:
                raise exceptions.InvalidOption(
                    "Enter valid availability [1/2]")
        except exceptions.InvalidOption as e:
            availability = None
            print(e)
        except ValueError:
            print("Enter valid availability [1/2]")

    rating = None
    while not rating:
        try:
            rating = int(input("Enter Rating : "))
            if rating not in [1, 2, 3, 4, 5]:
                raise exceptions.InvalidOption(
                    "Enter valid rating [1/2/3/4/5]")
        except exceptions.InvalidOption as e:
            rating = 0
            print(e)
        except ValueError:
            print("Enter valid rating [1/2/3/4/5]")

    ppp = None
    while not ppp:
        try:
            ppp = int(input("Enter Price per Plate : "))
        except ValueError:
            print("Enter valid Price per Plate.")

    cost = None
    while not cost:
        try:
            cost = int(input("Enter Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("insert into catering (name, city, contact, details, rating, availability, price_per_plate, cost) values (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (name, city, contact, details, rating, availability, ppp, cost))


def addPhotographer():
    print("Current data in Photographers :\n")
    photographers = pd.read_sql(
        "select * from photographer;", cnx).to_string(index=False)
    print(photographers)
    cursor.reset()

    name = None
    while not name:
        name = input("Enter Name : ")
        if name == "":
            print("Name cannot be empty")
            name = None

    city = None
    while not city:
        city = input("Enter City : ")
        if city == "":
            print("City cannot be empty.")
            city = None

    contact = None
    while not contact:
        try:
            contact = int(input("Enter Contact : "))
        except ValueError:
            print("Enter valid Contact")

    experience = None
    while not experience:
        experience = input("Enter Experience : ")
        if experience == "":
            print("Experience cannot be empty.")
            experience = None

    availability = None
    while not availability:
        try:
            availability = int(input("Enter Availability : "))
            if availability not in [1, 0]:
                raise exceptions.InvalidOption(
                    "Enter valid availability [1/2]")
        except exceptions.InvalidOption as e:
            availability = None
            print(e)
        except ValueError:
            print("Enter valid availability [1/2]")

    cost = None
    while not cost:
        try:
            cost = int(input("Enter Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("insert into photographer (name, city, contact, experience, availability, cost) values (%s, %s, %s, %s, %s, %s)",
                   (name, city, contact, experience, availability, cost))


def addMUA():
    print("Current data in Make-up Artists :\n")
    mua = pd.read_sql("select * from mua;", cnx).to_string(index=False)
    print(mua)
    cursor.reset()

    name = None
    while not name:
        name = input("Enter Name : ")
        if name == "":
            print("Name cannot be empty")
            name = None

    city = None
    while not city:
        city = input("Enter City : ")
        if city == "":
            print("City cannot be empty.")
            city = None

    contact = None
    while not contact:
        try:
            contact = int(input("Enter Contact : "))
        except ValueError:
            print("Enter valid Contact")

    experience = None
    while not experience:
        experience = input("Enter Experience : ")
        if experience == "":
            print("Experience cannot be empty.")
            experience = None

    availability = None
    while not availability:
        try:
            availability = int(input("Enter Availability : "))
            if availability not in [1, 0]:
                raise exceptions.InvalidOption(
                    "Enter valid availability [1/2]")
        except exceptions.InvalidOption as e:
            availability = None
            print(e)
        except ValueError:
            print("Enter valid availability [1/2]")

    cost = None
    while not cost:
        try:
            cost = int(input("Enter Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("insert into mua (name, city, contact, experience, availability, cost) values (%s, %s, %s, %s, %s, %s)",
                   (name, city, contact, experience, availability, cost))


def addLive():
    print("Current data in Concert Artists :\n")
    live = pd.read_sql("select * from live;", cnx).to_string(index=False)
    print(live)
    cursor.reset()

    name = None
    while not name:
        name = input("Enter Name : ")
        if name == "":
            print("Name cannot be empty")
            name = None

    city = None
    while not city:
        city = input("Enter City : ")
        if city == "":
            print("City cannot be empty.")
            city = None

    contact = None
    while not contact:
        try:
            contact = int(input("Enter Contact : "))
        except ValueError:
            print("Enter valid Contact")

    experience = None
    while not experience:
        experience = input("Enter Experience : ")
        if experience == "":
            print("Experience cannot be empty.")
            experience = None

    availability = None
    while not availability:
        try:
            availability = int(input("Enter Availability : "))
            if availability not in [1, 0]:
                raise exceptions.InvalidOption(
                    "Enter valid availability [1/2]")
        except exceptions.InvalidOption as e:
            availability = None
            print(e)
        except ValueError:
            print("Enter valid availability [1/2]")

    cost = None
    while not cost:
        try:
            cost = int(input("Enter Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("insert into live (name, city, contact, experience, availability, cost) values (%s, %s, %s, %s, %s, %s)",
                   (name, city, contact, experience, availability, cost))


def addDJ():
    print("Current data in DJs :\n")
    dj = pd.read_sql("select * from dj;", cnx).to_string(index=False)
    print(dj)
    cursor.reset()

    name = None
    while not name:
        name = input("Enter Name : ")
        if name == "":
            print("Name cannot be empty")
            name = None

    city = None
    while not city:
        city = input("Enter City : ")
        if city == "":
            print("City cannot be empty.")
            city = None

    contact = None
    while not contact:
        try:
            contact = int(input("Enter Contact : "))
        except ValueError:
            print("Enter valid Contact")

    experience = None
    while not experience:
        experience = input("Enter Experience : ")
        if experience == "":
            print("Experience cannot be empty.")
            experience = None

    availability = None
    while not availability:
        try:
            availability = int(input("Enter Availability : "))
            if availability not in [1, 0]:
                raise exceptions.InvalidOption(
                    "Enter valid availability [1/2]")
        except exceptions.InvalidOption as e:
            availability = None
            print(e)
        except ValueError:
            print("Enter valid availability [1/2]")

    cost = None
    while not cost:
        try:
            cost = int(input("Enter Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("insert into dj (name, city, contact, experience, availability, cost) values (%s, %s, %s, %s, %s, %s)",
                   (name, city, contact, experience, availability, cost))


def addEntertainment():
    print("Current data in Entertainment :\n")
    entertainment = pd.read_sql(
        "select * from entertainment;", cnx).to_string(index=False)
    print(entertainment)
    cursor.reset()

    name = None
    while not name:
        name = input("Enter Name : ")
        if name == "":
            print("Name cannot be empty")
            name = None

    city = None
    while not city:
        city = input("Enter City : ")
        if city == "":
            print("City cannot be empty.")
            city = None

    details = None
    while not details:
        details = input("Enter Details : ")
        if details == "":
            print("Details cannot be empty.")
            details = None

    cost = None
    while not cost:
        try:
            cost = int(input("Enter Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("insert into entertainment (name, city, details, cost) values (%s, %s, %s, %s, %s, %s)",
                   (name, city, details, cost))


def addAssistant():
    print("Current data in Assistants :\n")
    assistants = pd.read_sql(
        "select * from assistaints;", cnx).to_string(index=False)
    print(assistants)
    cursor.reset()

    name = None
    while not name:
        name = input("Enter Name : ")
        if name == "":
            print("Name cannot be empty")
            name = None

    city = None
    while not city:
        city = input("Enter City : ")
        if city == "":
            print("City cannot be empty.")
            city = None

    contact = None
    while not contact:
        try:
            contact = int(input("Enter Contact : "))
        except ValueError:
            print("Enter valid Contact")

    experience = None
    while not experience:
        experience = input("Enter Experience : ")
        if experience == "":
            print("Experience cannot be empty.")
            experience = None

    availability = None
    while not availability:
        try:
            availability = int(input("Enter Availability : "))
            if availability not in [1, 0]:
                raise exceptions.InvalidOption(
                    "Enter valid availability [1/2]")
        except exceptions.InvalidOption as e:
            availability = None
            print(e)
        except ValueError:
            print("Enter valid availability [1/2]")

    cursor.reset()
    cursor.execute("insert into assistants (name, city, contact, experience, availability) values (%s, %s, %s, %s, %s)",
                   (name, city, contact, experience, availability))


def updatePack():
    print("Current data in Curated Packs :\n")
    packs = pd.read_sql("select * from packs;", cnx).to_string(index=False)
    print(packs)
    cursor.reset()

    name = None
    while not name:
        name = input("Enter Name : ")
        if name == "":
            print("Name cannot be empty")
            name = None

    city = None
    while not city:
        city = input("Enter City : ")
        if city == "":
            print("City cannot be empty.")
            city = None

    details = None
    while not details:
        details = input("Enter Details : ")
        if details == "":
            print("Details cannot be empty.")
            details = None

    cost = None
    while not cost:
        try:
            cost = int(input("Enter Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("insert into packs (name, city, details, cost) values (%s, %s, %s, %s, %s, %s)",
                   (name, city, details, cost))
