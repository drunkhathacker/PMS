# Password Management System
# Start of the Program

from Functions import *

print("Enter your choice")
print("1. Login")
c = int(input("Manually check a password for leakage"))

while True:
    try:
        if c == 1:
            login()
        if c == 2:
            pwnd()
        break

    except ValueError:
        print("Please choose a valid option")
