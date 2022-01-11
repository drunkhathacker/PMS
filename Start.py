from Functions import *
# Login or create

print("Enter your choice")
print("1. Create user")
c = input("2.Login")  # add exception later

if c == 1:
    create()
if c == 2:
    login()
