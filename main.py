# Password Management System
# Start of the Program
from Functions import login, selfcheck


print("Enter your choice")
print("1. Login")
c = int(input("2.Manually check a password for leakage"))

try:
    if c == 1:
        login()
    if c == 2:
        selfcheck()

except ValueError:
    print("Please choose a valid option")


