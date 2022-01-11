import getpass
import hashlib
import os
import pickle
import random
import string
import sqlite3 as sl
import pwnedpasswords

con = sl.connect('my-test.db')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS USER (Website TEXT,Password TEXT )")


# Create a user
def create():
    userdata = dict()
    if os.path.exists('userinfo.pickle'):
        userdata = pickle.load(open('userinfo.pickle', 'rb'))
    username = input('Enter username:')
    pwd = getpass.getpass("Enter password:")
    pwd2 = getpass.getpass("Enter password again:")
    if pwd != pwd2:
        print("Passwords do not match")
        exit(0)
    h = hashlib.md5()
    h.update(pwd.encode('utf-8'))
    pwd = h.hexdigest()
    if username not in userdata:
        userdata[username] = pwd
    with open('userinfo.pickle', 'wb') as handle:
        pickle.dump(userdata, handle)
    con = sl.connect('my-test.db')
    c = con.cursor()
    query = 'CREATE TABLE IF NOT EXISTS {} (Website TEXT,Password TEXT )'.format(username)
    c.execute(query)


# Login the user

def login():
    userdata = pickle.load(open('userinfo.pickle', 'rb'))
    username = input("Enter username:")
    pwd = getpass.getpass("Enter password:")
    h = hashlib.md5()
    h.update(pwd.encode('utf-8'))
    pwd = h.hexdigest()
    if username in userdata:
        if userdata[username] == pwd:
            print("Success.")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

#Generate Password

def generate():
    len = int(input('Enter the length of the password'))
    print(len)  # Test
    characters = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(characters) for i in range(len))
    print(pwd)
    ans = input("Do you want to store this password to the database?; yes or no")
    ans = ans.lower()
    if ans == 'yes':
        site = input("Enter the name of the website")
        db(site, pwd)
    pwnd(pwd)


def db(s, p):
    c.execute("INSERT INTO PASS (Website,Password)VALUES (?,?)", (s, p))
    con.commit()


def showall():
    c.execute("SELECT * FROM PASS")
    result = c.fetchall()
    for x in result:
        print(x)


def pwnd(pd):
    if pwnedpasswords.check(pd) != 0:
        print("Hacked")
    else:
        print("Safe")


def batch():
    num = int(input("Enter the length of the passwords:"))
    times = int(input("How many passwords"))
    f = open("SavedPasswords.txt", "a")
    for x in range(times):
        chars = string.ascii_letters + string.digits + string.punctuation
        pewed = ''.join(random.choice(chars) for i in range(num))
        f.write("{0}\n".format(pewed))
    f.close()


def selfcheck():
    selb = input("Enter the password you want to check for leakage")
    pwnd(selb)

create()
