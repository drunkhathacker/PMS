# Logged in as admin
import string
import random

global min_length
global min_number
global min_upper
global min_special


def set_policy():
    min_length = input("Enter minimum length of the password")
    min_number = input("Enter minimum numerical characters in the password")
    min_upper = input("Enter minimum uppercase characters  in the password")
    min_special = input("Enter minimum number of special characters in the password")


def batch():
    times = int(input("How many passwords"))
    f = open("SavedPasswords.txt", "a")
    for x in range(times):
        upper = ''
        special = ''
        numb = ''
        for i in range(min_upper):
            upper = upper + string.ascii_uppercase
        for i in range(min_special):
            special = special + string.punctuation
        for i in range(min_number):
            numb = numb + string.digits
        characters = upper + special + numb + string.ascii_lowercase
        bpsswd = ''.join(random.choice(characters) for i in range(min_length))
        f.write("{0}\n".format(bpsswd))
    f.close()

# def view_all():
