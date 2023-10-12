## Problem Statement : Find the minimum number of given two numbers

## Conclusion : We will take 2 integers as input from user and check which is maximum among them 

## Algorithm :

'''
    START
        Create 2 variables value1 and value2
        Create Ret variable to store result
        get first number from user and store it in the value1
        get second number from user and store it in the value2
        if - value1 < value2 return value1
        or - return value2
    STOP
'''

#############################################################################################
##
##  Function Name : Minimum
##  Description :   Take two integer and returns maximum out of them 
##  Input :         Intger, integer
##  Output :        Integer
##  Author :        Ajay Yogesh Varma
##  Date :          12-10-2023
##
#############################################################################################

def Minimum (iNo1, iNo2):
    if(iNo1 < iNo2):
        return iNo1
    elif(iNo2 < iNo1):
        return iNo2

#############################################################################################
##
##  This is entry point of program
##
#############################################################################################

iValue1 = (int (input("Enter the first number : ")))
iValue2 = (int(input("Enter second number : ")))

iRet = Minimum(iValue1, iValue2)

print(f"Minimum number is {iRet}")