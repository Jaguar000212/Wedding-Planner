from . import helpers, exceptions, backend
import matplotlib.pyplot as plt
import numpy as np


def initLogger():
    helpers.clear()
    print(f"Welcome to this interactive Wedding Planner, Sir")
    print("Select an option to get started.\n1. Databases\n2. Visualisation\n3. Show Users\n4. Show Bookings\n5. Show Feedbacks\n6. Log-out")

    option = None
    while not option:
        try:
            option = int(input("Select option (1/2/3/4/5/6) : "))
            if option not in [1, 2, 3, 4, 5, 6]:
                raise exceptions.InvalidOption(
                    "Select from 1, 2, 3, 4, 5 or 6 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1, 2, 3, 4, 5 or 6 only")

    if option == 1:
        Databases()
    elif option == 2:
        showVisualisation()
    elif option == 3:
        showUsers()
    elif option == 4:
        showBookings()
    elif option == 5:
        viewFeedbacks()
    else:
        helpers.welcome()


def Databases():
    helpers.clear()
    print("Select an option and continue.\n1. Show Databases\n2. Edit Databases\n3. Add Data\n4. Delete Data\n5. Back")

    option = None
    while not option:
        try:
            option = int(input("Select option (1/2/3/4/5) : "))
            if option not in [1, 2, 3, 4, 5]:
                raise exceptions.InvalidOption(
                    "Select from 1, 2, 3, 4 or 5 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1, 2, 3, 4 or 5 only")

    if option == 1:
        init_showDatabases()
    elif option == 2:
        init_editDatabases()
    elif option == 3:
        init_addDatabases()
    elif option == 4:
        init_deleteDatabases()
    else:
        initLogger()


def init_showDatabases():
    helpers.clear()
    print("Select Database you want to have a look at.\n1. Venues\n2. Caterers\n3. Photographers\n4. Make-up Artist\n5. Concerts\n6. DJ\n7. Entertainment\n8. Assistants\n9. Curated Packs\n10. Partnered Services\n11. Back")
    option = None
    while not option:
        try:
            option = int(input("Select option (1/2/3/4/5/6/7/8/9/10/11) : "))
            if option not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                raise exceptions.InvalidOption(
                    "Select from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 or 11 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 or 11 only")
    if option == 1:
        showDatabase("venue")
    elif option == 2:
        showDatabase("catering")
    elif option == 3:
        showDatabase("photographer")
    elif option == 4:
        showDatabase("mua")
    elif option == 5:
        showDatabase("live")
    elif option == 6:
        showDatabase("dj")
    elif option == 7:
        showDatabase("entertainment")
    elif option == 8:
        showDatabase("assistants")
    elif option == 9:
        showDatabase("packs")
    elif option == 10:
        showDatabase("partnered")
    else:
        Databases()


def showDatabase(database):
    helpers.clear()
    backend.selData(database)
    input("\nPress Enter to get back. ")
    init_showDatabases()


def init_editDatabases():
    helpers.clear()
    print("Select Database you want to edit.\n1. Venues\n2. Caterers\n3. Photographers\n4. Make-up Artist\n5. Concerts\n6. DJ\n7. Entertainment\n8. Assistants\n9. Curated Packs\n10. Back")
    option = None
    while not option:
        try:
            option = int(input("Select option (1/2/3/4/5/6/7/8/9/10) : "))
            if option not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                raise exceptions.InvalidOption(
                    "Select from 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10 only")
    if option == 1:
        editDatabase("venue")
    elif option == 2:
        editDatabase("catering")
    elif option == 3:
        editDatabase("photographer")
    elif option == 4:
        editDatabase("mua")
    elif option == 5:
        editDatabase("live")
    elif option == 6:
        editDatabase("dj")
    elif option == 7:
        editDatabase("entertainment")
    elif option == 8:
        editDatabase("assistants")
    elif option == 9:
        showDatabase("packs")
    else:
        Databases()


def editDatabase(database):
    helpers.clear()
    if database == "venue":
        backend.updateVenue()
    elif database == "catering":
        backend.updateCaterer()
    elif database == "photographer":
        backend.updatePhotographer()
    elif database == "mua":
        backend.updateMUA()
    elif database == "live":
        backend.updateLive()
    elif database == "dj":
        backend.updateDJ()
    elif database == "entertainment":
        backend.updateEntertainment()
    elif database == "assistants":
        backend.updateAssistant()
    elif database == "packs":
        backend.updatePack()

    print("Data successfully edited.")
    input("Press Enter to get back. ")
    init_editDatabases()


def init_addDatabases():
    helpers.clear()
    print("Select Database you want to add data to.\n1. Venues\n2. Caterers\n3. Photographers\n4. Make-up Artist\n5. Concerts\n6. DJ\n7. Entertainment\n8. Assistants\n9. Curated Packs\n10. Back")
    option = None
    while not option:
        try:
            option = int(input("Select option (1/2/3/4/5/6/7/8/9/10) : "))
            if option not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                raise exceptions.InvalidOption(
                    "Select from 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10 only")
    if option == 1:
        addDatabase("venue")
    elif option == 2:
        addDatabase("catering")
    elif option == 3:
        addDatabase("photographer")
    elif option == 4:
        addDatabase("mua")
    elif option == 5:
        addDatabase("live")
    elif option == 6:
        addDatabase("dj")
    elif option == 7:
        addDatabase("entertainment")
    elif option == 8:
        addDatabase("assistants")
    elif option == 9:
        addDatabase("packs")
    else:
        Databases()


def addDatabase(database):
    helpers.clear()
    if database == "venue":
        backend.addVenue()
    elif database == "catering":
        backend.addCaterer()
    elif database == "photographer":
        backend.addPhotographer()
    elif database == "mua":
        backend.addMUA()
    elif database == "live":
        backend.addLive()
    elif database == "dj":
        backend.addDJ()
    elif database == "entertainment":
        backend.addEntertainment()
    elif database == "assistants":
        backend.addAssistant()
    elif database == "packs":
        backend.addPack()

    print("Data successfully added.")
    input("Press Enter to get back. ")
    init_addDatabases()


def init_deleteDatabases():
    helpers.clear()
    print("Select Database you want to delete data from.\n1. Venues\n2. Caterers\n3. Photographers\n4. Make-up Artist\n5. Concerts\n6. DJ\n7. Entertainment\n8. Assistants\n9. Curated Packs\n10. Back")
    option = None
    while not option:
        try:
            option = int(input("Select option (1/2/3/4/5/6/7/8/9/10) : "))
            if option not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                raise exceptions.InvalidOption(
                    "Select from 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10 only")
    if option == 1:
        deleteDatabase("venue")
    elif option == 2:
        deleteDatabase("catering")
    elif option == 3:
        deleteDatabase("photographer")
    elif option == 4:
        deleteDatabase("mua")
    elif option == 5:
        deleteDatabase("live")
    elif option == 6:
        deleteDatabase("dj")
    elif option == 7:
        deleteDatabase("entertainment")
    elif option == 8:
        deleteDatabase("assistants")
    elif option == 9:
        deleteDatabase("packs")
    else:
        Databases()


def deleteDatabase(database):
    helpers.clear()

    backend.deleteData(database)
    print("Data successfully deleted.")
    input("Press Enter to get back. ")
    init_deleteDatabases()


def showVisualisation():
    helpers.clear()
    print("Select data to be visualised.\n1. User Ratings\n2. Payment Data\n3. Popularity\n4. Back")
    option = None
    while not option:
        try:
            option = int(input("Select option (1/2/3/4) : "))
            if option not in [1, 2, 3, 4]:
                raise exceptions.InvalidOption("Select from 1, 2, 3 or 4 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1, 2, 3 or 4 only")

    if option == 1:
        data = backend.selRatings()
        color = []
        for d in data:
            color.append('orange')
            
        plt.hist(data, histtype='barstacked', color=color)
        plt.xticks([5, 4, 3, 2, 1])
        plt.ylabel("Ratings")
        plt.xlabel("Users")
        plt.title("Received Ratings")
        plt.show()
        showVisualisation()
    elif option == 2:
        data = backend.selAmount()
        plt.plot(data[0], marker = '*')
        plt.plot(data[1], marker = 'd')
        plt.xticks(list(range(len(data[1]))))
        plt.legend(["Estimated Total", "Amount Paid"])
        plt.ylabel("Amount in ₹")
        plt.xlabel("User")
        plt.title("Payment Data")
        plt.grid(True)
        plt.show()
        showVisualisation()
    elif option == 3:
        cities = ['Jaipur', 'Udaipur', 'Jodhpur', 'Jaisalmer']
        popularity = [31, 48, 11, 10]
        color = ['orange', 'y', 'red', 'blue']
        plt.bar(cities, popularity, color=color)
        plt.ylabel("Popularity in %")
        plt.xlabel("Cities")
        plt.title("City Popularity")
        plt.show()
        showVisualisation()
    else:
        initLogger()


def showUsers():
    helpers.clear()
    print("########### REGISTERED USERS ###########\n")
    backend.selUsers()
    input("\nPress Enter to get back. ")
    initLogger()


def showBookings():
    helpers.clear()
    print("########### USER BOOKINGS ###########\n")
    backend.selBookings()
    input("\nPress Enter to get back. ")
    initLogger()


def viewFeedbacks():
    helpers.clear()
    print("########### USER FEEDBACKS ###########\n")
    backend.selFeedbacks()
    input("\nPress Enter to get back. ")
    initLogger()
