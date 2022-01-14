import getpass
import hashlib
import os
import pickle
import random
import string
import sqlite3 as sl
import pwnedpasswords
from admin_functions import *

con = sl.connect('my-test.db')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS USER (Website TEXT,Password TEXT )")


# Create a user



# Login the user


#Generate Password

def generate():
    upper = ''
    special = ''
    numb = ''
    for i in range(min_upper):
        upper = upper + string.ascii_uppercase
    for i in range(min_special):
        special = special + string.punctuation
    for i in range(min_number):
        numb = numb + string.digits
    characters = upper+special+numb+string.ascii_lowercase
    pwd = ''.join(random.choice(characters) for i in range(min_length))
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

def selfcheck():
    selb = input("Enter the password you want to check for leakage")
    pwnd(selb)

def login():
    username = input("Enter your username:")
    pwd = getpass.getpass("Enter password")
    h = hashlib.md5()
    h.update(pwd.encode('utf-8'))
    pwd = h.hexdigest()
    con = sl.connect('my-test.db')
    c = con.cursor()
    query = "SELECT Role FROM MASTERED where Username='" + username + "' AND Password ='" + pwd + "'"
    c.execute(query)
    result = c.fetchall()
    # if result == 1:
    #     normal()
    # if result == 2:
    #     admin()
    for x in result:
        print(x)



