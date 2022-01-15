# Logged in as admin
import string
import random
import getpass
import sqlite3 as sl

global min_length
global min_number
global min_upper
global min_special
import hashlib

con = sl.connect('my-test.db')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS MASTERED (Username TEXT,Password TEXT, Role INTEGER )")



def set_policy():
    global min_length = input("Enter minimum length of the password")
    global min_number = input("Enter minimum numerical characters in the password")
    global min_upper = input("Enter minimum uppercase characters  in the password")
    global min_special =  input("Enter minimum number of special characters in the password")


def batch():
    times = int(input("How many passwords"))
    f = open("SavedPasswords.txt", "a")
    for x in range(times):
        upper = ''
        special = ''
        numb = ''
        for i in range(min_upper):
            upper = upper + string.ascii_uppercase
        for i in range(min_special):
            special = special + string.punctuation
        for i in range(min_number):
            numb = numb + string.digits
        characters = upper + special + numb + string.ascii_lowercase
        bpsswd = ''.join(random.choice(characters) for i in range(min_length))
        f.write("{0}\n".format(bpsswd))
    f.close()


# Create a user. Only admin can create a new user

def create():
    userdata = dict()
    username = input("Enter username")
    if username in userdata:  # Not Working, Use try except later
        print("User already Exists")
    pwd = getpass.getpass("Enter password:")
    pwd2 = getpass.getpass("Enter password again:")
    if pwd != pwd2:
        print("Passwords do not match")
        exit(0)
    h = hashlib.md5()
    h.update(pwd.encode('utf-8'))
    pwd = h.hexdigest()
    role = input("Set role code")
    ls = [pwd, role]
    userdata[username] = ls
    print(userdata)
    con = sl.connect('my-test.db')
    c = con.cursor()
    c.execute("INSERT INTO MASTERED (Username,Password,Role)VALUES (?,?,?)", (username, pwd, role))
    c.execute("CREATE TABLE IF NOT EXISTS {}(Username TEXT,Password TEXT)").__format__(username)
    con.commit()
