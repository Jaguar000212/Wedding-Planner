from . import helpers, exceptions, backend
import time
import json
import pandas as pd
from gui import DatePicker
import datetime as dt


def initLogger():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    print(f"Welcome to this interactive Wedding Planner, {TempData['name']}")
    print(f"Continue for the wedding of your dream...")
    print("NOTE : Your progress is unsaved until you confirm your booking.\nMake sure to confirm the booking before closing the program,\nor you may have to start over")
    time.sleep(3)
    getStatus()


def getStatus():
    status = backend.checkStatus()
    if status:
        helpers.clear()
        option = None
        print(
            "Do you want to :-\n1. Review your previous booking\n2. New Booking\n3. Log-out")
        while not option:
            try:
                option = int(input("Select option (1/2/3) : "))
                if option not in [1, 2, 3]:
                    raise exceptions.InvalidOption(
                        "Select from 1, 2, and 3 only")
            except exceptions.InvalidOption as e:
                option = 0
                print(e)
            except ValueError:
                print("Select from 1, 2, and 3 only")
        if option == 1:
            showBooking()
        elif option == 2:
            getCity(status)
        else:
            helpers.userWelcome()
    else:
        getCity(status)


def showBooking():
    helpers.clear()
    backend.selBooked()
    print("Select an option.\n1. Home\n2. Make Payment")
    option = None
    while not option:
        try:
            option = int(input("Select option (1/2) : "))
            if option not in [1, 2]:
                raise exceptions.InvalidOption("Select from 1 or 2 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1 or 2  only")

    if option == 1:
        getStatus()
    else:
        with open("data/temp.json", "r") as f:
            TempData = json.load(f)
        paid = backend.selAmount(TempData['sno'])
        payable = (paid[0][0] - paid[1][0])
        helpers.clear()

        if payable != 0:
            amount = None
            while not amount:
                try:
                    amount = int(input("Enter amount to be paid : "))
                    if amount > (payable):
                        raise exceptions.InvalidOption(
                            f"Enter amount less than or equal to ₹ {payable}")
                except exceptions.InvalidOption as e:
                    amount = 0
                    print(e)
                except ValueError:
                    print("Enter vaild amount")

            option = None
            while not option:
                try:
                    option = int(input(
                        "\nSelect you mode of payment.\n1. UPI\n2. Bank-Transfer\n3. Back\nSelect option : "))
                    if option not in [1, 2, 3]:
                        option = None
                        raise exceptions.InvalidOption("Select 1, 2 or 3 only")
                except ValueError:
                    raise exceptions.InvalidOption("Select 1, 2 or 3 only")
                except Exception as e:
                    print(e)
            
            with open("utils/config.json", "r") as f:
                config = json.load(f)

            if option == 1:
                print(
                    f"\nOur UPI ID is {config['bank']['upi']}. Please pay\n₹ {amount} with-in 5 minutes\nelse the transaction will be aborted.")
                input("Press Enter to Continue. ")
                backend.updatePaid(amount + paid[1][0])
                print(
                    f"\nSUCCESSFULLY PAID\nMode of Payment - UPI\nAmount Paid - ₹ {amount}")
                input("Press Enter to Continue. ")
                showBooking()

            elif option == 2:
                print(f"\n########### Bank A/c Details ############")
                print(f"Name ------------------- {config['bank']['name']}")
                print(f"Account Number --------- {config['bank']['ac']}")
                print(f"IFSC Code -------------- {config['bank']['ifsc']}")
                print(f"Amount to be Paid ------ ₹ {amount}")
                print(
                    f"Please pay ₹ {amount} with-in 5 minutes else the transaction will be aborted.")

                input("Press Enter to Continue. ")
                backend.updatePaid(amount + paid[1][0])
                print(
                    f"\nSUCCESSFULLY PAID\nMode of Payment - Bank-Transfer\nAmount Paid - ₹ {amount}")
                input("Press Enter to Continue. ")
                showBooking()

            else:
                showBooking()
        else:
            input("You have cleared all your dues. Press Enter to get back. ")
            showBooking()


def getCity(status):
    if status:
        back = "Back"
        back_func = getStatus
    else:
        back = "Log-out"
        back_func = helpers.userWelcome
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print(
        f"In which city the wedding will be?\nCurrently, we operate in selected cities.\n1. Jaipur\n2. Udaipur\n3. Jodhpur\n4. Jaisalmer\n5. {back}")
    while not option:
        try:
            option = int(input("Select option (1/2/3/4/5) : "))
            if option not in [1, 2, 3, 4, 5]:
                raise exceptions.InvalidOption(
                    "Select from 1, 2, 3, 4, and 5 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1, 2, 3, 4, and 5 only")
    if option == 1:
        TempData['city'] = "Jaipur"
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getDate()
    elif option == 2:
        TempData['city'] = "Udaipur"
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getDate()
    elif option == 3:
        TempData['city'] = "Jodhpur"
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getDate()
    elif option == 4:
        TempData['city'] = "Jaisalmer"
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getDate()
    elif option == 5:
        TempData['city'] = ""
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        back_func()


def getDate():
    helpers.clear()
    print("Select your wedding date from the dialog box.")

    DatePicker(getCity).mainloop()

    getGuests()


def getGuests():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    while not option:
        option = input(
            "Enter number of guests that will be attending the occasion or enter 'b' to get back. : ")
        try:
            guests = int(option)
        except ValueError:
            if option == 'b':
                getDate()
            else:
                option = None
                print("Enter numbers only")

    TempData['guests'] = guests
    with open("data/temp.json", "w") as f:
        json.dump(TempData, f, indent=4)

    getStarted()


def getStarted():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print("Do you want the wedding to be customised or choose from curated packages.\nCustomisation can give a clearer look to your dream but can take time.\nPackages are decent and budget friendly, can be best when time is running short.\n1. Customise\n2. Package\n3. Back")
    while not option:
        try:
            option = int(input("Select option (1/2/3) : "))
            if option not in [1, 2, 3]:
                raise exceptions.InvalidOption("Select from 1, 2 and 3 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1, 2 and 3 only")
    if option == 1:
        TempData['pack'] = "0"
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getVenue()
    elif option == 2:
        TempData['venue'] = "0"
        TempData['caterer'] = "0"
        TempData['photographer'] = "0"
        TempData['mua'] = "0"
        TempData['live'] = "0"
        TempData['dj'] = "0"
        TempData['entertainment'] = "0"
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getPack()
    elif option == 3:
        getGuests()


def getPack():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print("Select the pack best suitable for you\nand the rest worry is ours.\nEnter the Serial Number of the Pack\nor 'b' to get back to last menu.\n")
    print()
    backend.selPack()
    print()
    while not option:
        try:
            option = input("Select option : ")
            if option not in [str(i) for i in range(1, 100)] + ['b']:
                raise exceptions.InvalidOption("Select from SNo. only")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select from SNo. only")
    if option == "b":
        getStarted()
    else:
        TempData['pack'] = option
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        showData()


def getVenue():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print("Select your desired Venue for the wedding\nEnter the Serial Number of the Venue\nor 'b' to get back to last menu\nor 0 to skip this service.")
    print()
    backend.selVenue()
    print()
    print("NOTE : Total price is the cost as well as Price-per-Plate calculated after wedding.\n")
    while not option:
        try:
            option = input("Select option : ")
            if option not in [str(i) for i in range(100)] + ['b']:
                raise exceptions.InvalidOption("Select from SNo. only")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select from SNo. only")
    if option == "b":
        getStarted()
    else:
        TempData['venue'] = option
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getCater()


def getCater():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print("Select your desired Caterer for the wedding\nEnter the Serial Number of the Caterer\nSkip the service if you have selected the Venue.\nor 'b' to get back to last menu\nor 0 to skip this service.")
    print()
    backend.selCaterer()
    print()
    while not option:
        try:
            option = input("Select option : ")
            if option not in [str(i) for i in range(100)] + ['b']:
                raise exceptions.InvalidOption("Select from SNo. only")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select from SNo. only")
    if option == "b":
        getVenue()
    else:
        TempData['caterer'] = option
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getPhotographer()


def getPhotographer():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print("Select your desired Photographer for the wedding\nEnter the Serial Number of the Photographer\nor 'b' to get back to last menu\nor 0 to skip this service.")
    print()
    backend.selPhotographer()
    print()
    while not option:
        try:
            option = input("Select option : ")
            if option not in [str(i) for i in range(100)] + ['b']:
                raise exceptions.InvalidOption("Select from SNo. only")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select from SNo. only")
    if option == "b":
        getCater()
    else:
        TempData['photographer'] = option
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getMUA()


def getMUA():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print("Select your desired Make-up Artist for the wedding\nEnter the Serial Number of the Artist\nor 'b' to get back to last menu\nor 0 to skip this service.")
    print()
    backend.selMUA()
    print()
    while not option:
        try:
            option = input("Select option : ")
            if option not in [str(i) for i in range(100)] + ['b']:
                raise exceptions.InvalidOption("Select from SNo. only")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select from SNo. only")
    if option == "b":
        getPhotographer()
    else:
        TempData['mua'] = option
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getLive()


def getLive():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print("Select your desired Live Concert for the wedding\nEnter the Serial Number of the Artist\nor 'b' to get back to last menu\nor 0 to skip this service.")
    print()
    backend.selLive()
    print()
    while not option:
        try:
            option = input("Select option : ")
            if option not in [str(i) for i in range(100)] + ['b']:
                raise exceptions.InvalidOption("Select from SNo. only")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select from SNo. only")
    if option == "b":
        getMUA()
    else:
        TempData['live'] = option
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getDJ()


def getDJ():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print("Select your desired DJ for the wedding\nEnter the Serial Number of the DJ\nor 'b' to get back to last menu\nor 0 to skip this service.")
    print()
    backend.selDJ()
    print()
    while not option:
        try:
            option = input("Select option : ")
            if option not in [str(i) for i in range(100)] + ['b']:
                raise exceptions.InvalidOption("Select from SNo. only")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select from SNo. only")
    if option == "b":
        getLive()
    else:
        TempData['dj'] = option
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getEntertainment()


def getEntertainment():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print("Select your desired Entertainment Service for the wedding\nEnter the Serial Number of the Service\nor 'b' to get back to last menu\nor 0 to skip this service.")
    print()
    backend.selEntertainment()
    print()
    while not option:
        try:
            option = input("Select option : ")
            if option not in [str(i) for i in range(100)] + ['b']:
                raise exceptions.InvalidOption("Select from SNo. only")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select from SNo. only")
    if option == "b":
        getDJ()
    else:
        TempData['entertainment'] = option
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)
        getDecor()


def getDecor():
    helpers.clear()
    option = None
    print("We provide Decor services but we are partnered\nwith some 3rd parties to get you an exotic decor for your wedding.\nWe are providing you the details of some of our partners.\nFeel free to contact them.\nSelect 1 to continue or 'b' to get back.")
    print()
    backend.selDecor()
    print()
    while not option:
        try:
            option = input("Select option : ")
            if option not in ['1', 'b']:
                raise exceptions.InvalidOption("Select 1 to Continue")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select 1 to Continue")
    if option == "b":
        getEntertainment()
    else:
        getJeweller()


def getJeweller():
    helpers.clear()
    option = None
    print("We provide Jewelleries but we are partnered\nwith some top-quality Jewellers of the City.\nWe are providing you the details of some of our partners.\nFeel free to contact them.\nSelect 1 to continue or 'b' to get back.")
    print()
    backend.selJeweller()
    print()
    while not option:
        try:
            option = input("Select option : ")
            if option not in ['1', 'b']:
                raise exceptions.InvalidOption("Select 1 to Continue")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select 1 to Continue")
    if option == "b":
        getDecor()
    else:
        showData()


def showData():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print(f"######## Your Selected Options ########\n")
    print(f"City ----------------- {TempData['city']}")

    if TempData['pack'] != "0":
        data = backend.selPackData()
        back_func = getPack
        print(f"Curated Pack --------- {data[0]}\n")
        print(f"Details :-\n{data[1]}\n")
    else:
        data = backend.selCustomData()
        back_func = getJeweller
        print(f"Venue ---------------- {data[0][0]}")
        print(f"Caterer -------------- {data[1][0]}")
        print(f"Photographer --------- {data[2][0]}")
        print(f"Make-up Artist ------- {data[3][0]}")
        print(f"Concert -------------- {data[4][0]}")
        print(f"DJ ------------------- {data[5][0]}")
        print(f"Entertainment -------- {data[6][0]}\n")

    print("1. Continue\n2. Back")
    while not option:
        try:
            option = int(input("Select option : "))
            if option not in [1, 2]:
                raise exceptions.InvalidOption("Select 1 or 2 only")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select 1 or 2 only")
    if option == 1:
        showBill()
    else:
        back_func()


def genBill():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)

    data = backend.selCustomData()
    pack = backend.selPackData()

    if TempData['pack'] != "0":
        cost = pack[2]
        dfDict = {
            pack[0]: {
                'Details': pack[1],
                'Cost': pack[2]
            }
        }
    else:
        cost = 0
        for service in data:
            price = service[1]
            if price is None:
                price = 00.00
            cost += price
        cCost = TempData['ppp'] * TempData['guests']

        dfDict = {
            'Venue': {
                'Name': data[0][0],
                'Cost': f"₹ {data[0][1]}"
            },
            'Caterer': {
                'Name': data[1][0],
                'Cost': f"₹ {data[1][1]}"
            },
            'Photographer': {
                'Name': data[2][0],
                'Cost': f"₹ {data[2][1]}"
            },
            'Make-up Artist': {
                'Name': data[3][0],
                'Cost': f"₹ {data[3][1]}"
            },
            'Concert': {
                'Name': data[4][0],
                'Cost': f"₹ {data[4][1]}"
            },
            'DJ': {
                'Name': data[5][0],
                'Cost': f"₹ {data[5][1]}"
            },
            'Entertainment': {
                'Name': data[6][0],
                'Cost': f"₹ {data[6][1]}"
            }
        }

    dF = (pd.DataFrame(dfDict)).T

    print(f"Name -------------- {TempData['name']}")
    print(f"City -------------- {TempData['city']}")
    print(f"Contact ----------- {TempData['contact']}")
    print(f"E-Mail ------------ {TempData['email']}")
    print(f"Booking Date ------ {dt.date.today()}")
    print(f"Wedding Date ------ {TempData['date']}")
    print(f"Guests ------------ {TempData['guests']}")
    print(f"\n{dF.to_string()}\n")

    if TempData['pack'] == "0":
        print(f"Price-per-Plate for Catering = ₹ {TempData['ppp']}")
        print(f"Estimated Surplus Catering Charges = ₹ {cCost}")
        total = cost + 5000.00 + cCost
        rtrn = (cost, cCost)
    else:
        total = cost + 5000.00
        rtrn = (cost, 00.00)
    print(f"Estimated Charges = ₹ {float(cost)}")
    print(f"Service Charges = ₹ 5000.00")
    print(f"Tax and Other Charges = ₹ 00.00")
    print(f"Estimated Total = ₹ {total}")

    print("\n#### CONDITIONS ####\n1. Total stated here is subject to change depending upon the final order.\n3. Amount to be paid for booking is 25% of Estimated Total.\n3. 50% of the payment should be done 10 days before the final day of wedding and rest should be paid before the same day.\n4. A Personal Assisstant will be appointed to you after the booking for further consultion.\n5. You won't be able to edit your changes after booking.\n\n")

    TempData['total'] = total
    with open("data/temp.json", "w") as f:
        json.dump(TempData, f, indent=4)

    return rtrn


def showBill():
    helpers.clear()
    option = None
    bill = genBill()
    print("By continuing, you agree to above stated Conditions.\n1. Continue\n2. Back")
    while not option:
        try:
            option = int(input("Select option : "))
            if option not in [1, 2]:
                raise exceptions.InvalidOption("Select 1 or 2 only")
        except exceptions.InvalidOption as e:
            option = None
            print(e)
        except ValueError:
            print("Select 1 or 2 only")
    if option == 1:
        payBill((bill[0] + 5000.00 + bill[1])/4)
    else:
        showData()


def payBill(amt):
    with open("utils/config.json", "r") as f:
        config = json.load(f)

    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    helpers.clear()
    option = None
    print(
        f"Dear customer, to confirm your booking, amount of ₹ {amt} needs to be paid.")
    while not option:
        try:
            option = int(input(
                "Select you mode of payment.\n1. UPI\n2. Bank-Transfer\n3. Back\nSelect option : "))
            if option not in [1, 2, 3]:
                option = None
                raise exceptions.InvalidOption("Select 1, 2 or 3 only")
        except ValueError:
            raise exceptions.InvalidOption("Select 1, 2 or 3 only")
        except Exception as e:
            print(e)
    if option == 1:
        print(
            f"\nOur UPI ID is {config['bank']['upi']}. Please pay\n₹ {amt} with-in 5 minutes of generation of bill\nelse the transaction will be aborted.")

        input("\nPress Enter to Continue. ")
        helpers.clear()
        genBill()
        print(
            f"SUCCESSFULLY BOOKED\nMode of Payment - UPI\nAmount Paid - ₹ {amt}")

        TempData['paid'] = amt
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)

        backend.updateData()

        option = None
        while not option:
            try:
                option = int(
                    input("Press 1 to share us your precious feedback or press 2 to skip : "))
                if option not in [1, 2]:
                    option = None
                    raise exceptions.InvalidOption("Select 1 or 2")
            except ValueError:
                option = None
                print("Select 1 or 2")
            except exceptions.InvalidOption as e:
                print(e)

        if option == 1:
            getFeedback()
        else:
            getStatus()

    elif option == 2:
        print(f"\n########### Bank A/c Details ############")
        print(f"Name ------------------- {config['bank']['name']}")
        print(f"Account Number --------- {config['bank']['ac']}")
        print(f"IFSC Code -------------- {config['bank']['ifsc']}")
        print(f"Amount to be Paid ------ ₹ {amt}")
        print("\nPlease pay the bill with-in 5 minutes of its generation else the transaction will be aborted.")

        input("Press Enter to Continue. ")
        helpers.clear()
        genBill()
        print(
            f"SUCCESSFULLY BOOKED\nMode of Payment - Bank-Transfer\nAmount Paid - ₹ {amt}")

        TempData['paid'] = amt
        with open("data/temp.json", "w") as f:
            json.dump(TempData, f, indent=4)

        backend.updateData()

        option = None
        while not option:
            try:
                option = int(
                    input("\n\nPress 1 to share us your precious feedback or press 2 to skip : "))
                if option not in [1, 2]:
                    option = None
                    raise exceptions.InvalidOption("Select 1 or 2")
            except ValueError:
                option = None
                print("Select 1 or 2")
            except exceptions.InvalidOption as e:
                print(e)

        if option == 1:
            getFeedback()
        else:
            getStatus()

    else:
        showBill()


def getFeedback():
    helpers.clear()
    print("Thank you for sparing some time with your precious feedback.")
    stars = None
    while not stars:
        try:
            stars = int(input("Give us some stars [1/2/3/4/5] : "))
            if stars not in [1, 2, 3, 4, 5]:
                stars = None
                raise exceptions.InvalidOption("Select from 1, 2, 3, 4 or 5")
        except ValueError:
            stars = None
            print("Select from 1, 2, 3, 4 or 5")
        except Exception as e:
            print(e)

    feedback = input("Brief us your experience :-\n")
    backend.addFeedback(stars, feedback)
    input("Your feedback has been recorded.\nPress Enter to get back to Home.")
    getStatus()
