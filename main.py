# Password Management System
# Start of the Program

print("Enter your choice")
print("1. Create user")
c = int(input("2.Login"))

while True:
    try:
        if c == 1:
            print("Create")
        if c == 2:
            print("Login")
        break

    except ValueError:
        print("Please choose a valid option")
