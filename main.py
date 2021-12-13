import random
import string
import sqlite3 as sl
import pwnedpasswords

con = sl.connect('my-test.db')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS PASS (Website TEXT,Password TEXT )")


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


# generate()
# showall()
# batch()
selfcheck()
