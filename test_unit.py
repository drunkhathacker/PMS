import unittest

import pwnedpasswords
import config
import secrets
import string
import string_utils

def pwnd(pd):
    if pwnedpasswords.check(pd) != 0:
        print("Hacked")
    else:
        print("Safe")

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
    pword = string_utils.shuffle(pword)
    return pword


class Test_length(unittest.TestCase):
    def setUp(self):
        print("Sanjkdsnkjsdcnja")
        self.length = 8

    def test_length(self):
        x = len(generate())
        print(x)
        self.assertEqual(x, self.length)
    def test_complex(self):
        password=generate()
        cupper=0
        clower=0
        cspecial=0
        cnumber= 0
        for x in password:
            if x.islower():
                clower+=1
            if x.isupper():
                cupper+=1
            if x.isnumeric():
                cnumber+=1
            if x in string.punctuation:
                cspecial+=1
        self.assertEqual(cupper,config.min_upper)
        self.assertEqual(cnumber,config.min_number)
        self.assertEqual(cspecial,config.min_special)


class Test_pwn(unittest.TestCase):
    def setUp(self):
        self.safe = 0

    def test_length(self):
        x=pwnd("iloveyou")
        print(x)
        self.assertNotEqual(x, self.safe)


if __name__ == "__main__":
    unittest.main()
