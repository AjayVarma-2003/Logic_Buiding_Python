## Problem Statement : Take 3 integers as input from user and return their average 

## Conclusion : We will take three integers as input and perform their average as (No 1 + No2 + No3)/ 3

## Algorithm : 

'''
    START 
        create 3 variables as no1, no2, no3
        take 3 integer values as input from user and store it in those variables
        create variable result to store result of average
        perform (no1 + no2 + no3)/3 and store its value in result
        return result
    STOP
'''

#############################################################################################
##
##  Function Name : Average
##  Description :   Takes 3 intgers and returns their average
##  Input :         Integer, Integer, Integer
##  Output :        float
##  Author :        Ajay Yogesh Varma
##  Date :          12-10-2023
##
#############################################################################################

def Average (iNo1 , iNo2, iNo3):
    fResult = (float(iNo1) + float(iNo2) + float(iNo3)) / 3
    return fResult

#############################################################################################
##
##  This is entry point of program
##
#############################################################################################

iValue1 = (int(input("Enter the first number : ")))
iValue2 = (int(input("Enter the second number : ")))
iValue3 = (int(input("Enter the third number : ")))

iRet = Average(iValue1, iValue2, iValue3)

print(f"Average of the number is {iRet}")