#!/usr/bin/python

##########################################
#
#               L O O P S
#
##########################################

import getpass


while True:
    secret_password = getpass.getpass("Please enter the password: ")
    if secret_password == "spicy cheetos":
        print "C O N G R A T U L A T I O N"
        break
    else:
        print "I N C O R R E C T !"
