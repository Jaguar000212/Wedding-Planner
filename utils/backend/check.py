import mysql.connector as mysql
import json

with open("utils/config.json", "r") as f:
    config = json.load(f)

cnx = mysql.connect(user=config['mysql']['user'],
                    password=config['mysql']['password'],
                    database=config['mysql']['database'])
cnx.autocommit = True
cursor = cnx.cursor()


def checkUser(username: str, password: str):
    cursor.reset()
    cursor.execute(
        "select username, password from user_data where username = %s and password = %s", (username, password))
    if (username, password) in cursor:
        return True
    return False


def checkStatus():
    with open("data/temp.json", "r") as f:
        TempData = json.load(f)
    cursor.reset()
    cursor.execute(
        "select booked from user_data where SNo = %s;", (TempData['sno'],))
    result = cursor.fetchone()
    try:
        if result[0] == 1:
            return True
        return False
    except:
        return False
