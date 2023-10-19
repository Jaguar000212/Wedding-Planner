import time
import mysql.connector as mysql
import json


def start():
    import utils
    utils.helpers.welcome()


try:
    start()
except mysql.errors.InterfaceError:
    print("MySQL is not running.\nStart MySQL to continue.")
except Exception as e:
    print("An error occured!")
    print(f"\n### Error ###\n{e}")
    time.sleep(2)
finally:
    print("Deleting temporary data...")
    tempData = {}
    with open("data/temp.json", "w") as f:
        json.dump(tempData, f, indent=4)
    time.sleep(1)

    print("Exiting program...")
    time.sleep(1)
