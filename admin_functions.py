# Logged in as admin
import string
import secrets
import getpass
import sqlite3 as sl
import config
import hashlib
import string_utils

con = sl.connect('/Users/sandhu/PycharmProjects/PasswordManagementSystem/my-test.db')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS MASTERED (Username TEXT,Password TEXT, Role INTEGER )")


def set_policy():

    config.min_length = int(input("Enter minimum length of the password"))
    config.min_number = int(input("Enter minimum numerical characters in the password"))
    config.min_upper = int(input("Enter minimum uppercase characters  in the password"))
    config.min_special = int(input("Enter minimum number of special characters in the password"))
    config.min_lower = int(input("Enter minimum number of lowercase characters in the password"))



def batch():
    times = int(input("How many passwords"))
    f = open("SavedPasswords.txt", "a")
    for x in range(times):
        print("*******Generating new password*******")
        global key
        upper = string.ascii_uppercase
        special = string.punctuation
        numb = string.digits
        lower = string.ascii_lowercase
        pword = ''
        for i in range(config.min_upper):
            n = secrets.randbelow(26)
            pword = pword + upper[n]
        for i in range(config.min_special):
            n = secrets.randbelow(10)
            pword = pword + special[n]
        for i in range(config.min_number):
            n = secrets.randbelow(10)
            pword = pword + numb[n]
        for i in range(config.min_lower):
            n = secrets.randbelow(26)
            pword = pword + lower[n]
        pworddd = string_utils.shuffle(pword)
        f.write("{0}\n".format(pworddd))
    f.close()


# Create a user. Only admin can create a new user

def create():
    userdata = dict()
    username = input("Enter username")
    con = sl.connect('/Users/sandhu/PycharmProjects/PasswordManagementSystem/my-test.db')
    c = con.cursor()
    c.execute(("SELECT * FROM MASTERED"))
    R=c.fetchall()
    if username in R:
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
    con = sl.connect('/Users/sandhu/PycharmProjects/PasswordManagementSystem/my-test.db')
    c = con.cursor()
    c.execute("INSERT INTO MASTERED (Username,Password,Role)VALUES (?,?,?)", (username, pwd, role))
    c.execute("CREATE TABLE [%s](Website,Password,key)"%username)
    con.commit()

def deli():
    con = sl.connect('/Users/sandhu/PycharmProjects/PasswordManagementSystem/my-test.db')
    c = con.cursor()
    c.execute("SELECT USERNAME FROM MASTERED")
    tresult = c.fetchall()
    for x in tresult:
        print(x)
    usrrr = input("Select the user you want to delete")
    c.execute("DROP TABLE "+usrrr)

def view_tables():
    con = sl.connect('/Users/sandhu/PycharmProjects/PasswordManagementSystem/my-test.db')
    c = con.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())



