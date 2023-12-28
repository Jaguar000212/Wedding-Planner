from os import system, name
from gui import *
import json
import sys
from . import exceptions, adminLogger


def welcome():
    tempData = {

    }

    with open("data/temp.json", "w") as f:
        json.dump(tempData, f, indent=4)

    clear()
    print('##############################################\n############## WEDDING PLANNER ###############\n##############################################')
    print('\nSelect the login option to continue!\n1. User\n2. Admin\n3. Exit')

    option = 0

    while not option:
        try:
            option = int(input("Select option (1/2/3) : "))
            if option not in [1, 2, 3]:
                raise exceptions.InvalidOption("Select 1 or 2 or 3 only")
        except exceptions.InvalidOption as e:
            option = 0
            print(e)
        except ValueError:
            print("Select from 1 or 2 or 3 only")

    if option == 1:
        userWelcome()
    elif option == 2:
        clear()
        print("Please continue on the window")
        # AdminLoginGUI(back_func=welcome).mainloop()
        adminLogger.initLogger()
    elif option == 3:
        sys.exit()


def userWelcome():
    clear()
    option = None
    print("Login or Register?\n1. Login\n2. Register\n3. Delete Account\n4. Back")
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
    print("Please continue on the window")
    if option == 1:
        UserLoginGUI(back_func=userWelcome).mainloop()
    elif option == 2:
        UserRegisterGUI(back_func=userWelcome).mainloop()
    elif option == 3:
        UserDeleteGUI(back_func=userWelcome).mainloop()
    else:
        welcome()


def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
