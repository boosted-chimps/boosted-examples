#!/usr/bin/python
###########################
#
#  Loops.py
#
###########################

import getpass


while True:
    secret_password = getpass.getpass("Please enter the password:")
    
    if secret_password == "Theodore":
        print "Congratulations, you've won!"
        break
    else:
        print "The password is incorrect."
