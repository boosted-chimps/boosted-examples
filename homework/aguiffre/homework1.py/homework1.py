#Homework1 - aguiffre
#Defining functions / Palindromes

def paladin_drome(string):

    if string[::-1] == string:

        return True
        
    else:

        return False


#second function
#paladin_drome_lists


def paladin_drome_lists(lists):

    for string in lists:

        if paladin_drome(string):

            print "%s is a palindrome!" % string
    

        
#call timez
#chyeah

paladin_drome_lists(["racecar", "seknankes","dookinbuttz"])

        

    
        
