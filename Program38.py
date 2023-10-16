## Problem Statement : Take a number as a integer and check whether it is prime or not

## Conclusion : We will find the number is prime or not using for loop iteration and if-else condition checking

## Algorithm :
'''
    START
        take a number as input from user and store it in variable 
        if number is less than 0 then return false
        iterate the for loop till the number to find the number has factor or not
        if number has no factors then return true
        else return false
    STOP
'''

###########################################################################################################
##
##  Function Name : CheckPrime
##  Description :   Takes a number as input and checks whether it is prime or not
##  Input :         Integer
##  Output :        boolean
##  Author :        Ajay Yogesh Varma
##  Date :          16-10-2023
##
############################################################################################################

def CheckPrime (iNo):
    bFlag = True
    if(iNo < 0):
        return False
    for iCnt in range (2, int(iNo / 2)+1):
        if(iNo % iCnt == 0):
            bFlag = False
            break
    
    return bFlag

############################################################################################################
##
##  This is entry point of the function
##
############################################################################################################

iValue = (int(input("Enter the number : ")))

iRet = CheckPrime(iValue)

if(iRet == True):
    print(f"{iValue} is a prime number ")
else:
    print(f"{iValue} is not a prime number ")