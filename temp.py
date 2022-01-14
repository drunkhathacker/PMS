import getpass
import hashlib
import sqlite3 as sl

con = sl.connect('my-test.db')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS MASTERED (Username TEXT,Password TEXT, Role INTEGER )")


def create():
    userdata = dict()
    username = input("Enter username")
    if username in userdata:                 # Not Working, Use try except later
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
    #c.execute("INSERT INTO MASTERED (Username,Password,Role)VALUES (?,?,?)", (username, pwd, role))
    c.execute("CREATE TABLE IF NOT EXISTS "+ username +"(Username TEXT,Password TEXT)")
    con.commit()


def show():
    c.execute("SELECT * FROM sqlite_master")
    result = c.fetchall()
    for x in result:
        print(x)


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

def normal():
    print("Logged in as a normal user \n")
    print("You have the following options: \n")
    print("1. Create a new password")
    print("2. Show existing passwords")

#create()
show()

#login()
