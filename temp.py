# import getpass
# import hashlib
# import sqlite3 as sl
import config
import string
import secrets
import string_utils


#
# con = sl.connect('my-test.db')
# c = con.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS MASTERED (Username TEXT,Password TEXT, Role INTEGER )")
#
#
# def create():
#     userdata = dict()
#     username = input("Enter username")
#     if username in userdata:                 # Not Working, Use try except later
#         print("User already Exists")
#     pwd = getpass.getpass("Enter password:")
#     pwd2 = getpass.getpass("Enter password again:")
#     if pwd != pwd2:
#         print("Passwords do not match")
#         exit(0)
#     h = hashlib.md5()
#     h.update(pwd.encode('utf-8'))
#     pwd = h.hexdigest()
#     role = input("Set role code")
#     ls = [pwd, role]
#     userdata[username] = ls
#     print(userdata)
#     con = sl.connect('my-test.db')
#     c = con.cursor()
#     #c.execute("INSERT INTO MASTERED (Username,Password,Role)VALUES (?,?,?)", (username, pwd, role))
#     c.execute("CREATE TABLE IF NOT EXISTS "+ username +"(Username TEXT,Password TEXT)")
#     con.commit()
#
#
# def show():
#     c.execute("SELECT * FROM sqlite_master")
#     result = c.fetchall()
#     for x in result:
#         print(x)
#
#
# def login():
#     username = input("Enter your username:")
#     pwd = getpass.getpass("Enter password")
#     h = hashlib.md5()
#     h.update(pwd.encode('utf-8'))
#     pwd = h.hexdigest()
#     con = sl.connect('my-test.db')
#     c = con.cursor()
#     query ="SELECT ROLE FROM MASTERED WHERE Username='" + username + "'AND Password ='" + pwd +"'"
#     c.execute(query)
#     result = c.fetchone()
#     new = result[0]
#     print(type(new))
#     if new == 1:
#         normal(Username)
#     if new == 2:
#          admin()
#     for x in result:
#         print(x)
#
# # def normal():
# #     print("Logged in as a normal user \n")
# #     print("You have the following options: \n")
# #     print("1. Create a new password")
# #     c= input("2. Show existing passwords")
# #     if c==1:
# #         generate()
# #     if c==2:
#
#
def generate():
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
        print(pword)
    pword = string_utils.shuffle(pword)
    print(pword)

def set_policy():

    config.min_length = int(input("Enter length of the password"))
    config.min_number = int(input("Enter minimum numerical characters in the password"))
    config.min_upper = int(input("Enter minimum uppercase characters  in the password"))
    config.min_special = int(input("Enter minimum number of special characters in the password"))
    config.min_lower = int(input("Enter minimum number of lowercase characters in the password"))
    print(config.min_upper)
    print(config.min_number)

set_policy()
generate()
# #create()
# #show()
# #create()
# #login()
