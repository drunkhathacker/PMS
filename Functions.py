import getpass
import hashlib
import secrets
import unittest
import string
import sqlite3 as sl
import pwnedpasswords
from admin_functions import *
import config
from cryptography.fernet import Fernet
import string_utils



#Generate Password

def generate(name):
    print("*******Generating new password*******")
    global key
    upper = string.ascii_uppercase
    special = string.punctuation
    numb = string.digits
    lower= string.ascii_lowercase
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
    pword = string_utils.shuffle(pword)
    print(pword)
    ans = input("Do you want to store this password to the database?; y or n?")
    ans = ans.lower()
    if ans == 'y':
        key = Fernet.generate_key()
        site = input("Enter the name of the website")
        pwd = encrypt_password(pword)
        db(name,site, pword,key)


def db(usname,s, p, k):
    c.execute("INSERT INTO " + usname +" (Website,Password, Key)VALUES (?,?,?) ", (s, p,k))
    con.commit()



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
    con = sl.connect('/Users/sandhu/PycharmProjects/PasswordManagementSystem/my-test.db')
    c = con.cursor()
    query ="SELECT ROLE FROM MASTERED WHERE Username='" + username + "'AND Password ='" + pwd +"'"
    c.execute(query)
    result = c.fetchone()
    new = result[0]
    if new == 2:
        normal(username)
    if new == 1:
        admin()
    for x in result:
        print(x)


def normal(uname):
    print("*******Logged in as User")
    print("Updated Version")
    print(" You have the following options:")
    print("1. View your passwords")
    print("2. Create your passwords")
    print("3. To exit")
    print("Updated Version")
    choice = int(input("Enter your choice"))
    print(choice)
    print(type(choice))
    if choice == 1:
        conx = sl.connect('/Users/sandhu/PycharmProjects/PasswordManagementSystem/my-test.db')
        cx = conx.cursor()
        query = "SELECT * FROM " + uname
        cx.execute(query)
        result = cx.fetchall()
        for x in result:
            print(x)
    elif choice == 2:
        generate(uname)
    elif choice == 3:
        exit()



def admin():
    print("********Logged in as admin********")
    print(" You have the following options:")
    print("1. Change password policy")
    print("2. Create batch passwords")
    print("3. Create a user account")
    print("4. Delete a user account")
    i = int(input("Enter your choice"))
    if i == 1:
        set_policy()
    elif i == 2:
        batch()
    elif i == 3:
        create()
    elif i == 4:
        deli()



# Function to encrypt Password
def encrypt_password(password):
    password = password.encode()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(password)
    return cipher_text

# Function to decrypt password
def decrypt_password(cipher_text, key):
    cipher_suite = Fernet(key)
    unciphered_text = (cipher_suite.decrypt(cipher_text))
    return unciphered_text

def view_mastered():
    con = sl.connect('/Users/sandhu/PycharmProjects/PasswordManagementSystem/my-test.db')
    c = con.cursor()
    query = "SELECT * FROM MASTERED"
    c.execute(query)
    tp = c.fetchall()
    print(tp)


