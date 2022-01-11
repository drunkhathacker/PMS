import getpass
import hashlib
import os
import pickle
import random
import string
import sqlite3 as sl
import pwnedpasswords


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


create()
