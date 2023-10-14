## Problem Statement : Take a 2 number from user as input and find if the 2nd number is factor of fiest number 

## Conclusion : We have to find the factor of number using for loop and if else condition checking

## Algorithm :

'''
    START 
        Take a 2 numbers from user as input and store it in variables
        check if 1st number is divisible by 2nd number then it is factor of 1st number
        if not then return false
    STOP
'''

############################################################################################
##
##  Function Name : CheckFactor  
##  Input :         Integer, Integer
##  Output :        boolean
##  Description :   Takes two numbers and checks whether 2nd number is factor of 1st number
##  Author :        Ajay Yogesh Varma
##  Date :          13-10-2023
##
############################################################################################

def CheckFactor (iNo1 , iNo2):
    if(iNo1 % iNo2 == 0):
        return True
    else:
        return False

############################################################################################
##
##  This is entry point of function
##
############################################################################################

iValue1 = (int(input("Enter the first number : ")))
iValue2 = (int (input("Enter the 2nd number : ")))

iRet = CheckFactor(iValue1, iValue2)

if(iRet == True):
    print(f"{iValue2} is factor of {iValue1}")
else:
    print(f"{iValue2} is not factor of {iValue1}")
