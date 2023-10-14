## Problem Statement : Take a integer as input and check whether it is prime number or not

## Coclusion : Perfect number is number that is equal to the sum of its factors excluding the number itself
##              so to find number we will add the factors of number and check it by if-else condition checking

## Algorithm :

'''
    START 
        Take a integer as a input and store it in variable
        use for loop and iterate it till the number to find factors
        add factors and store it in variable 
        if sum variable is equal to the input variable then return true
    STOP
'''

############################################################################################
##
##  Function Name : CheckPerfect
##  Description :   It takes the integer as input and checks whether it is perfect number or not
##  Input :         Integer
##  Output :        bolean
##  Author :        Ajay Yogesh Varma
##  Date :          14-10-2023
##
############################################################################################

def CheckPerfect(iNo):
    iSum = 0
    
    for iCnt in range (1, iNo):
        if(iNo % iCnt == 0):
            iSum += iCnt
    
    if(iSum == iNo):
        return True
    else:
        return False

############################################################################################
##
##  This is entry point of function
##
############################################################################################

iValue = (int (input("Enter the number : ")))

iRet = CheckPerfect(iValue)

if(iRet == True):
    print(f"{iValue} is perfect number")
else:
    print(f"{iValue} is not a perfect number")

