import mysql.connector as mysql
import pandas as pd
import json
import warnings

warnings.filterwarnings('ignore')
with open("utils/config.json", "r") as f:
    config = json.load(f)

cnx = mysql.connect(user=config['mysql']['user'],
                    password=config['mysql']['password'],
                    database=config['mysql']['database'])
cnx.autocommit = True
cursor = cnx.cursor()


def selUserData(username, password):
    cursor.reset()
    cursor.execute(
        "select * from user_data where username = %s and password = %s", (username, password))
    data = cursor.fetchone()
    return data


def selPack():
    print(pd.read_sql("select SNo, Name, Details, Cost from packs;", cnx).to_string(index=False))


def selVenue():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    print(pd.read_sql("select SNo, Name, City, Address, Type, Rating, Size, Price_per_Plate, Cost from venue where City = '%s' and Availability = 1;" % (
        TempData['city'],), cnx).to_string(index=False))


def selCaterer():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    print(pd.read_sql("select SNo, Name, City, Contact, Details, Rating, Price_per_Plate, Cost from catering where City = '%s' and Availability = 1;" % (
        TempData['city'],), cnx).to_string(index=False))


def selPhotographer():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    print(pd.read_sql("select SNo, Name, City, Contact, Experience, Cost from photographer where City = '%s' and Availability = 1;" % (
        TempData['city'],), cnx).to_string(index=False))


def selMUA():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    print(pd.read_sql("select SNo, Name, City, Contact, Experience, Cost from mua where City = '%s' and Availability = 1;" % (
        TempData['city'],), cnx).to_string(index=False))


def selLive():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    print(pd.read_sql("select SNo, Name, City, Contact, Experience, Cost from live where City = '%s' and Availability = 1;" % (
        TempData['city'],), cnx).to_string(index=False))


def selDJ():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    print(pd.read_sql("select SNo, Name, City, Contact, Experience, Cost from dj where City = '%s' and Availability = 1;" % (
        TempData['city'],), cnx).to_string(index=False))


def selEntertainment():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    print(pd.read_sql("select SNo, Name, Cost from entertainment where City = '%s';" % (
        TempData['city'],), cnx).to_string(index=False))


def selDecor():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    df = pd.read_csv("data/partnered.csv")
    df = df[df['Type'] == 'Decor']
    df = df[df['City'] == TempData["city"]]
    print(df.loc[:, 'Name':'City'].to_string(index=False))


def selJeweller():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    df = pd.read_csv("data/partnered.csv")
    df = df[df['Type'] == 'Jeweller']
    df = df[df['City'] == TempData["city"]]
    print(df.loc[:, 'Name':'City'].to_string(index=False))


def selPackData():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    cursor.reset()
    cursor.execute(
        "select Name, Details, Cost from packs where SNo = %s", (int(TempData['pack']),))
    result = cursor.fetchone()
    if not result is None:
        return result
    return ("No Data Found", "Invalid Request. Get back and reselect the pack. Ensure to Enter correct SNo.", 00.00)


def selCustomData():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    data = []

    try:
        cursor.reset()
        cursor.execute("select Name, Cost from Venue where SNo = %s",
                       (int(TempData['venue']),))
        result = cursor.fetchone()
        if not result is None:
            data.append(result)
        else:
            data.append(["Skipped", 00.00])

        cursor.reset()
        cursor.execute(
            "select price_per_plate from Venue where SNo = %s", (int(TempData['venue']),))
        result = cursor.fetchone()
        if not result is None:
            TempData['ppp'] = result[0]
        else:
            TempData['ppp'] = 00.00
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
    except:
        pass

    try:
        cursor.reset()
        cursor.execute(
            "select Name, Cost from catering where SNo = %s", (int(TempData['caterer']),))
        result = cursor.fetchone()
        if not result is None:
            data.append(result)
        else:
            data.append(["Skipped", 00.00])

        cursor.reset()
        cursor.execute(
            "select price_per_plate from catering where SNo = %s", (int(TempData['caterer']),))
        result = cursor.fetchone()
        if not result is None:
            TempData['ppp'] = result[0]
        else:
            if TempData['ppp'] == 0:
                TempData['ppp'] = 00.00
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
    except:
        pass

    try:
        cursor.reset()
        cursor.execute("select Name, Cost from photographer where SNo = %s", (int(
            TempData['photographer']),))
        result = cursor.fetchone()
        if not result is None:
            data.append(result)
        else:
            data.append(["Skipped", 00.00])
    except:
        pass

    try:
        cursor.reset()
        cursor.execute("select Name, Cost from mua where SNo = %s",
                       (int(TempData['mua']),))
        result = cursor.fetchone()
        if not result is None:
            data.append(result)
        else:
            data.append(["Skipped", 00.00])
    except:
        pass

    try:
        cursor.reset()
        cursor.execute("select Name, Cost from live where SNo = %s",
                       (int(TempData['live']),))
        result = cursor.fetchone()
        if not result is None:
            data.append(result)
        else:
            data.append(["Skipped", 00.00])
    except:
        pass

    try:
        cursor.reset()
        cursor.execute("select Name, Cost from dj where SNo = %s",
                       (int(TempData['dj']),))
        result = cursor.fetchone()
        if not result is None:
            data.append(result)
        else:
            data.append(["Skipped", 00.00])
    except:
        pass

    try:
        cursor.reset()
        cursor.execute("select Name, Cost from entertainment where SNo = %s", (int(
            TempData['entertainment']),))
        result = cursor.fetchone()
        if not result is None:
            data.append(result)
        else:
            data.append(["Skipped", 00.00])
    except:
        pass

    return data


def selBooked():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)

    services = []

    cursor.reset()
    cursor.execute("select * from user_data where SNo = %s",
                   (TempData['sno'],))

    data = cursor.fetchone()

    cursor.reset()
    cursor.execute(
        "select name, details, cost from packs where sno = %s", (data[10],))
    pack = cursor.fetchone()

    cursor.reset()
    cursor.execute(
        "select name, cost, price_per_plate from Venue where sno = %s", (data[11],))
    venue = cursor.fetchone()
    if venue is None:
        venue = ("Skipped", 00.00, 00.00)

    cursor.reset()
    cursor.execute(
        "select name, cost, price_per_plate from catering where sno = %s", (data[12],))
    caterer = cursor.fetchone()
    if caterer is None:
        caterer = ("Skipped", 00.00, 00.00)

    cursor.reset()
    cursor.execute(
        "select name, cost from photographer where sno = %s", (data[12],))
    photographer = cursor.fetchone()
    if photographer is None:
        photographer = ("Skipped", 00.00)

    cursor.reset()
    cursor.execute("select name, cost from mua where sno = %s", (data[13],))
    mua = cursor.fetchone()
    if mua is None:
        mua = ("Skipped", 00.00)

    cursor.reset()
    cursor.execute("select name, cost from live where sno = %s", (data[14],))
    live = cursor.fetchone()
    if live is None:
        live = ("Skipped", 00.00)

    cursor.reset()
    cursor.execute("select name, cost from dj where sno = %s", (data[15],))
    dj = cursor.fetchone()
    if dj is None:
        dj = ("Skipped", 00.00)

    cursor.reset()
    cursor.execute(
        "select name, cost from Entertainment where sno = %s", (data[11],))
    entertainment = cursor.fetchone()
    if entertainment is None:
        entertainment = ("Skipped", 00.00)

    ppp = venue[2]
    if ppp == 0:
        ppp = caterer[2]

    services.append(venue)
    services.append(caterer)
    services.append(photographer)
    services.append(mua)
    services.append(live)
    services.append(dj)
    services.append(entertainment)

    if not pack is None:
        cost = pack[2]
        dfDict = {
            pack[0]: {
                'Details': pack[1],
                'Cost': pack[2]
            }
        }
    else:
        cost = 0
        for service in services:
            price = service[1]
            if price is None:
                price = 00.00
            cost += price
        cCost = ppp * data[9]

        dfDict = {
            'Venue': {
                'Name': venue[0],
                'Cost': f"₹ {venue[1]}"
            },
            'Caterer': {
                'Name': caterer[0],
                'Cost': f"₹ {caterer[1]}"
            },
            'Photographer': {
                'Name': photographer[0],
                'Cost': f"₹ {photographer[1]}"
            },
            'Make-up Artist': {
                'Name': mua[0],
                'Cost': f"₹ {mua[1]}"
            },
            'Concert': {
                'Name': live[0],
                'Cost': f"₹ {live[1]}"
            },
            'DJ': {
                'Name': dj[0],
                'Cost': f"₹ {dj[1]}"
            },
            'Entertainment': {
                'Name': entertainment[0],
                'Cost': f"₹ {entertainment[1]}"
            }
        }

    dF = (pd.DataFrame(dfDict)).T

    print(f"Name -------------- {data[1]}")
    print(f"City -------------- {data[7]}")
    print(f"Contact ----------- {data[4]}")
    print(f"E-Mail ------------ {data[5]}")
    print(f"Wedding Date ------ {data[8]}")
    print(f"Guests ------------ {data[9]}")
    print(f"\n{dF.to_string()}\n")

    if pack is None:
        print(f"Price-per-Plate for Catering = ₹ {ppp}")
        print(f"Estimated Surplus Catering Charges = ₹ {cCost}")
        total = cost + 5000.00 + cCost
    else:
        total = cost + 5000.00
    print(f"Estimated Charges = ₹ {float(cost)}")
    print(f"Service Charges = ₹ 5000.00")
    print(f"Tax and Other Charges = ₹ 00.00")
    print(f"Estimated Total = ₹ {total}")
    print(f"Amount Paid = ₹ {data[-1]}")

    print("\n#### CONDITIONS ####\n1. Total stated here is subject to change depending upon the final order.\n3. Amount to be paid for booking is 25% of Estimated Total.\n3. 50% of the payment should be done 10 days before the final day of wedding and rest should be paid before the same day.\n4. A Personal Assisstant will be appointed to you after the booking for further consultion.\n\n")


def selFeedbacks():
    print(pd.read_sql("select * from feedbacks", cnx).to_string())


def selUsers():
    print(pd.read_sql("select Name, Contact, E_mail from user_data;", cnx))


def selBookings():
    cursor.reset()
    cursor.execute("select * from user_data;")
    users = cursor.fetchall()
    dfDict = {
        'Name': [],
        'Contact': [],
        'E-Mail': [],
        'Booked': [],
        'City': [],
        'Date': [],
        'Guests': [],
        'Pack': [],
        'Venue': [],
        'Caterer': [],
        'Photographer': [],
        'Make-up Artist': [],
        'Concert': [],
        'DJ': [],
        'Entertainment': [],
        'Estimated Total': [],
        'Amount Paid': []
    }

    for user in users:
        dfDict['Name'].append(user[1])
        dfDict['Contact'].append(user[4])
        dfDict['E-Mail'].append(user[5])
        dfDict['Booked'].append(user[6])
        dfDict['City'].append(user[7])
        dfDict['Date'].append(user[8])
        dfDict['Guests'].append(user[9])
   
        cursor.reset()
        cursor.execute("select name from packs where sno = %s", (user[10],))
        pack = cursor.fetchone()
        if pack is not None:
            dfDict['Pack'].append(pack[0])
        else:
            dfDict['Pack'].append("Skipped")

        cursor.reset()
        cursor.execute("select name from venue where sno = %s", (user[11],))
        Venue = cursor.fetchone()
        if Venue is not None:
            dfDict['Venue'].append(Venue[0])
        else:
            dfDict['Venue'].append("Skipped")

        cursor.reset()
        cursor.execute("select name from catering where sno = %s", (user[12],))
        caterer = cursor.fetchone()
        if caterer is not None:
            dfDict['Caterer'].append(caterer[0])
        else:
            dfDict['Caterer'].append("Skipped")

        cursor.reset()
        cursor.execute(
            "select name from Photographer where sno = %s", (user[13],))
        Photographer = cursor.fetchone()
        if Photographer is not None:
            dfDict['Photographer'].append(Photographer[0])
        else:
            dfDict['Photographer'].append("Skipped")

        cursor.reset()
        cursor.execute("select name from mua where sno = %s", (user[14],))
        mua = cursor.fetchone()
        if mua is not None:
            dfDict['Make-up Artist'].append(mua[0])
        else:
            dfDict['Make-up Artist'].append("Skipped")

        cursor.reset()
        cursor.execute("select name from live where sno = %s", (user[15],))
        Concert = cursor.fetchone()
        if Concert is not None:
            dfDict['Concert'].append(Concert[0])
        else:
            dfDict['Concert'].append("Skipped")

        cursor.reset()
        cursor.execute("select name from DJ where sno = %s", (user[16],))
        DJ = cursor.fetchone()
        if DJ is not None:
            dfDict['DJ'].append(DJ[0])
        else:
            dfDict['DJ'].append("Skipped")

        cursor.reset()
        cursor.execute(
            "select name from Entertainment where sno = %s", (user[17],))
        Entertainment = cursor.fetchone()
        if Entertainment is not None:
            dfDict['Entertainment'].append(Entertainment[0])
        else:
            dfDict['Entertainment'].append("Skipped")

        dfDict['Estimated Total'].append(user[18])
        dfDict['Amount Paid'].append(user[19])

    print(pd.DataFrame(dfDict))


def selData(database):
    if database == "partnered":
        print(pd.read_csv("data/partnered.csv"))
    else:
        print(pd.read_sql("select * from %s;" %
              (database,), cnx).to_string(index=False))


def selRatings():
    cursor.reset()
    cursor.execute("select stars from feedbacks")
    return cursor.fetchall()


def selAmount(sno=None):
    if sno is None:
        cursor.reset()
        cursor.execute(
            "select estimatedtotal from user_data where estimatedtotal != 0")
        total = cursor.fetchall()

        cursor.reset()
        cursor.execute("select paid from user_data where estimatedtotal != 0")
        paid = cursor.fetchall()

    else:
        cursor.reset()
        cursor.execute(
            "select estimatedtotal from user_data where sno = %s", (sno,))
        total = cursor.fetchone()

        cursor.reset()
        cursor.execute("select paid from user_data where sno = %s", (sno,))
        paid = cursor.fetchone()

    return (total, paid)

# def selCityData():
