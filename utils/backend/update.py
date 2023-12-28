import mysql.connector as mysql
import json
import pandas as pd
from .. import exceptions

with open("utils/config.json", "r") as f:
    config = json.load(f)

cnx = mysql.connect(user=config['mysql']['user'],
                    password=config['mysql']['password'],
                    database=config['mysql']['database'])
cnx.autocommit = True
cursor = cnx.cursor(buffered=True)


def updateData():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    cursor.reset()
    try:
        cursor.execute("update user_data set booked = 1, city = %s, date = %s, guests = %s, pack = %s, venue = %s, caterer = %s, photographer = %s, mua = %s, live = %s, dj = %s, entertainment = %s, estimatedtotal = %s, paid = %s where SNo = %s;", (
            TempData["city"], TempData["date"], TempData["guests"], TempData["pack"], TempData["venue"], TempData["caterer"], TempData["photographer"], TempData["mua"], TempData["live"], TempData["dj"], TempData["entertainment"], TempData['total'], TempData['paid'], TempData['sno']))
        return True
    except Exception as e:
        print(e)
        return False


def updateVenue():
    print("Current data in Venues :\n")
    venues = pd.read_sql("select * from venue;", cnx).to_string(index=False)
    print(venues)
    print("\nNOTE : Enter blank to skip that option from editing.\n")
    cursor.reset()

    sno = None
    while not sno:
        try:
            sno = int(input("Select SNo to edit : "))
            cursor.execute("select * from venue where sno = %s", (sno,))
            result = cursor.fetchone()
            if result is None:
                raise exceptions.InvalidOption("Enter valid SNo.")
        except exceptions.InvalidOption as e:
            sno = 0
            print(e)
        except ValueError:
            print("Enter valid SNo.")

    name = input("Enter edited Name : ")
    if name == "":
        name = result[1]

    city = input("Enter edited City : ")
    if city == "":
        city = result[2]

    address = input("Enter edited Address : ")
    if address == "":
        address = result[3]

    vtype = input("Enter edited Type : ")
    if vtype == "":
        vtype = result[4]

    rating = None
    while not rating:
        try:
            rating = int(input("Enter edited Rating : "))
            if rating not in [1, 2, 3, 4, 5]:
                raise exceptions.InvalidOption(
                    "Enter valid rating [1/2/3/4/5]")
        except exceptions.InvalidOption as e:
            rating = 0
            print(e)
        except ValueError:
            print("Enter valid rating [1/2/3/4/5]")

    size = input("Enter edited Size : ")
    if size == "":
        size = result[6]

    availability = None
    while not availability:
        try:
            availability = int(input("Enter edited Availability : "))
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
            ppp = int(input("Enter edited Price per Plate : "))
        except ValueError:
            print("Enter valid Price per Plate.")

    cost = None
    while not cost:
        try:
            cost = int(input("Enter edited Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("update venue set name = %s, city = %s, address = %s, type = %s, rating = %s, size = %s, availability = %s, price_per_plate = %s, cost = %s where sno = %s",
                   (name, city, address, vtype, rating, size, availability, ppp, cost, sno))


def updateCaterer():
    print("Current data in Caterers :\n")
    caterers = pd.read_sql("select * from catering;",
                           cnx).to_string(index=False)
    print(caterers)
    print("\nNOTE : Enter blank to skip that option from editing.\n")
    cursor.reset()

    sno = None
    while not sno:
        try:
            sno = int(input("Select SNo to edit : "))
            cursor.execute("select * from catering where sno = %s", (sno,))
            result = cursor.fetchone()
            if result is None:
                raise exceptions.InvalidOption("Enter valid SNo.")
        except exceptions.InvalidOption as e:
            sno = 0
            print(e)
        except ValueError:
            print("Enter valid SNo.")

    name = input("Enter edited Name : ")
    if name == "":
        name = result[1]

    city = input("Enter edited City : ")
    if city == "":
        city = result[2]

    contact = None
    while not contact:
        try:
            contact = int(input("Enter edited Contact : "))
        except ValueError:
            print("Enter valid Contact")

    details = input("Enter edited Details : ")
    if details == "":
        details = result[4]

    availability = None
    while not availability:
        try:
            availability = int(input("Enter edited Availability : "))
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
            rating = int(input("Enter edited Rating : "))
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
            ppp = int(input("Enter edited Price per Plate : "))
        except ValueError:
            print("Enter valid Price per Plate.")

    cost = None
    while not cost:
        try:
            cost = int(input("Enter edited Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("update catering set name = %s, city = %s, contact = %s, details = %s, rating = %s, availability = %s, price_per_plate = %s, cost = %s where sno = %s",
                   (name, city, contact, details, rating, availability, ppp, cost, sno))


def updatePhotographer():
    print("Current data in Photographers :\n")
    photographers = pd.read_sql(
        "select * from photographer;", cnx).to_string(index=False)
    print(photographers)
    print("\nNOTE : Enter blank to skip that option from editing.\n")
    cursor.reset()

    sno = None
    while not sno:
        try:
            sno = int(input("Select SNo to edit : "))
            cursor.execute("select * from photographer where sno = %s", (sno,))
            result = cursor.fetchone()
            if result is None:
                raise exceptions.InvalidOption("Enter valid SNo.")
        except exceptions.InvalidOption as e:
            sno = 0
            print(e)
        except ValueError:
            print("Enter valid SNo.")

    name = input("Enter edited Name : ")
    if name == "":
        name = result[1]

    city = input("Enter edited City : ")
    if city == "":
        city = result[2]

    contact = None
    while not contact:
        try:
            contact = int(input("Enter edited Contact : "))
        except ValueError:
            print("Enter valid Contact")

    experience = input("Enter edited Experience : ")
    if experience == "":
        experience = result[4]

    availability = None
    while not availability:
        try:
            availability = int(input("Enter edited Availability : "))
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
            cost = int(input("Enter edited Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("update photographer set name = %s, city = %s, contact = %s, experience = %s, availability = %s, cost = %s where sno = %s",
                   (name, city, contact, experience, availability, cost, sno))


def updateMUA():
    print("Current data in Make-up Artists :\n")
    mua = pd.read_sql("select * from mua;", cnx).to_string(index=False)
    print(mua)
    print("\nNOTE : Enter blank to skip that option from editing.\n")
    cursor.reset()

    sno = None
    while not sno:
        try:
            sno = int(input("Select SNo to edit : "))
            cursor.execute("select * from mua where sno = %s", (sno,))
            result = cursor.fetchone()
            if result is None:
                raise exceptions.InvalidOption("Enter valid SNo.")
        except exceptions.InvalidOption as e:
            sno = 0
            print(e)
        except ValueError:
            print("Enter valid SNo.")

    name = input("Enter edited Name : ")
    if name == "":
        name = result[1]

    city = input("Enter edited City : ")
    if city == "":
        city = result[2]

    contact = None
    while not contact:
        try:
            contact = int(input("Enter edited Contact : "))
        except ValueError:
            print("Enter valid Contact")

    experience = input("Enter edited Experience : ")
    if experience == "":
        experience = result[4]

    availability = None
    while not availability:
        try:
            availability = int(input("Enter edited Availability : "))
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
            cost = int(input("Enter edited Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("update mua set name = %s, city = %s, contact = %s, experience = %s, availability = %s, cost = %s where sno = %s",
                   (name, city, contact, experience, availability, cost, sno))


def updateLive():
    print("Current data in Concert Artists :\n")
    live = pd.read_sql("select * from live;", cnx).to_string(index=False)
    print(live)
    print("\nNOTE : Enter blank to skip that option from editing.\n")
    cursor.reset()

    sno = None
    while not sno:
        try:
            sno = int(input("Select SNo to edit : "))
            cursor.execute("select * from live where sno = %s", (sno,))
            result = cursor.fetchone()
            if result is None:
                raise exceptions.InvalidOption("Enter valid SNo.")
        except exceptions.InvalidOption as e:
            sno = 0
            print(e)
        except ValueError:
            print("Enter valid SNo.")

    name = input("Enter edited Name : ")
    if name == "":
        name = result[1]

    city = input("Enter edited City : ")
    if city == "":
        city = result[2]

    contact = None
    while not contact:
        try:
            contact = int(input("Enter edited Contact : "))
        except ValueError:
            print("Enter valid Contact")

    experience = input("Enter edited Experience : ")
    if experience == "":
        experience = result[4]

    availability = None
    while not availability:
        try:
            availability = int(input("Enter edited Availability : "))
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
            cost = int(input("Enter edited Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("update live set name = %s, city = %s, contact = %s, experience = %s, availability = %s, cost = %s where sno = %s",
                   (name, city, contact, experience, availability, cost, sno))


def updateDJ():
    print("Current data in DJs :\n")
    dj = pd.read_sql("select * from dj;", cnx).to_string(index=False)
    print(dj)
    print("\nNOTE : Enter blank to skip that option from editing.\n")
    cursor.reset()

    sno = None
    while not sno:
        try:
            sno = int(input("Select SNo to edit : "))
            cursor.execute("select * from dj where sno = %s", (sno,))
            result = cursor.fetchone()
            if result is None:
                raise exceptions.InvalidOption("Enter valid SNo.")
        except exceptions.InvalidOption as e:
            sno = 0
            print(e)
        except ValueError:
            print("Enter valid SNo.")

    name = input("Enter edited Name : ")
    if name == "":
        name = result[1]

    city = input("Enter edited City : ")
    if city == "":
        city = result[2]

    contact = None
    while not contact:
        try:
            contact = int(input("Enter edited Contact : "))
        except ValueError:
            print("Enter valid Contact")

    experience = input("Enter edited Experience : ")
    if experience == "":
        experience = result[4]

    availability = None
    while not availability:
        try:
            availability = int(input("Enter edited Availability : "))
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
            cost = int(input("Enter edited Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("update dj set name = %s, city = %s, contact = %s, experience = %s, availability = %s, cost = %s where sno = %s",
                   (name, city, contact, experience, availability, cost, sno))


def updateEntertainment():
    print("Current data in Entertainment :\n")
    entertainment = pd.read_sql(
        "select * from entertainment;", cnx).to_string(index=False)
    print(entertainment)
    print("\nNOTE : Enter blank to skip that option from editing.\n")
    cursor.reset()

    sno = None
    while not sno:
        try:
            sno = int(input("Select SNo to edit : "))
            cursor.execute("select * from live where sno = %s", (sno,))
            result = cursor.fetchone()
            if result is None:
                raise exceptions.InvalidOption("Enter valid SNo.")
        except exceptions.InvalidOption as e:
            sno = 0
            print(e)
        except ValueError:
            print("Enter valid SNo.")

    name = input("Enter edited Name : ")
    if name == "":
        name = result[1]

    city = input("Enter edited City : ")
    if city == "":
        city = result[2]

    details = input("Enter edited Details : ")
    if details == "":
        details = result[4]

    cost = None
    while not cost:
        try:
            cost = int(input("Enter edited Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("update entertainment set name = %s, city = %s, details = %s, cost = %s where sno = %s",
                   (name, city, details, cost, sno))


def updateAssistant():
    print("Current data in Assistants :\n")
    assistants = pd.read_sql(
        "select * from assistaints;", cnx).to_string(index=False)
    print(assistants)
    print("\nNOTE : Enter blank to skip that option from editing.\n")
    cursor.reset()

    sno = None
    while not sno:
        try:
            sno = int(input("Select SNo to edit : "))
            cursor.execute("select * from live where sno = %s", (sno,))
            result = cursor.fetchone()
            if result is None:
                raise exceptions.InvalidOption("Enter valid SNo.")
        except exceptions.InvalidOption as e:
            sno = 0
            print(e)
        except ValueError:
            print("Enter valid SNo.")

    name = input("Enter edited Name : ")
    if name == "":
        name = result[1]

    city = input("Enter edited City : ")
    if city == "":
        city = result[2]

    contact = None
    while not contact:
        try:
            contact = int(input("Enter edited Contact : "))
        except ValueError:
            print("Enter valid Contact")

    experience = input("Enter edited Experience : ")
    if experience == "":
        experience = result[4]

    availability = None
    while not availability:
        try:
            availability = int(input("Enter edited Availability : "))
            if availability not in [1, 0]:
                raise exceptions.InvalidOption(
                    "Enter valid availability [1/2]")
        except exceptions.InvalidOption as e:
            availability = None
            print(e)
        except ValueError:
            print("Enter valid availability [1/2]")

    cursor.reset()
    cursor.execute("update assistants set name = %s, city = %s, contact = %s, experience = %s, availability = %s where sno = %s",
                   (name, city, contact, experience, availability, sno))


def updatePack():
    print("Current data in Curated Packs :\n")
    packs = pd.read_sql("select * from packs;", cnx).to_string(index=False)
    print(packs)
    print("\nNOTE : Enter blank to skip that option from editing.\n")
    cursor.reset()

    sno = None
    while not sno:
        try:
            sno = int(input("Select SNo to edit : "))
            cursor.execute("select * from live where sno = %s", (sno,))
            result = cursor.fetchone()
            if result is None:
                raise exceptions.InvalidOption("Enter valid SNo.")
        except exceptions.InvalidOption as e:
            sno = 0
            print(e)
        except ValueError:
            print("Enter valid SNo.")

    name = input("Enter edited Name : ")
    if name == "":
        name = result[1]

    city = input("Enter edited City : ")
    if city == "":
        city = result[2]

    details = input("Enter edited Details : ")
    if details == "":
        details = result[4]

    cost = None
    while not cost:
        try:
            cost = int(input("Enter edited Cost : "))
        except ValueError:
            print("Enter valid Cost.")

    cursor.reset()
    cursor.execute("update packs set name = %s, city = %s, details = %s, cost = %s where sno = %s",
                   (name, city, details, cost, sno))


def updatePaid(amt):
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)

    cursor.reset()
    cursor.execute("update user_data set paid = %s where sno = %s",
                   (amt, TempData["sno"]))
