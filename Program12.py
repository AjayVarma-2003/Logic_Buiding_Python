# Problem Statement : Take number from user and check whether it is odd or even

# Step 1: Understand the problem statement 
# Conclusion : Take number from user and find is it odd or even 

# Step 2 : Write Algorithm
'''
    START
        Accpet number by user
        divide given number by 2
        if reminder is equal to 0 display even
        or display odd
    STOP
'''

#dont do this program like this ... for correct way check progra,12.py

#############################################################################################
##
##  Function Name : CheckEven
##  Description :   Takes number from user as input and checks is is even or odd
##  Input :         integer
##  Output :        integer
##  Author Name :   Ajay Yogesh Varma
##  Date :          7-10-2023
##
#############################################################################################

def CheckEven (iValue):
    if(iValue % 2 == 0):
        return True
    else:
        return False    
        
#############################################################################################
##
##  This is entry point of program
##
#############################################################################################
        
iNo = 0
bRet = False

iNo = (int(input("Enter the number : ")))

bRet = CheckEven(iNo)

if (bRet == True):
    print("This is even number...")
else :
    print("This is odd number...")

