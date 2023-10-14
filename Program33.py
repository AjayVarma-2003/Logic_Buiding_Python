## Problem Statement : Take a number from user and return its factors 

## Conclusion : We will take integer as input from user and find its factors using for loop and if-else condtion checking

## Algorithm :

'''
    START
        Take a integer as input from user and store it in variable 
        iterate for loop till that number to find factor
        if number is fully divisible by any int then return it as factor
    STOP
'''

############################################################################################
##
##  Function Name : DisplayFactor
##  Description :   It takes integer as input and returns its factors
##  Input :         Integer
##  Output :        none
##  Author :        Ajay Yogesh Varma
##  Date :          14-10-2023
##
############################################################################################

def DisplayFactor(iNo):
    print("Factors of given numbers are : ")
    for iCnt in range(1, iNo+1):
        if(iNo % iCnt == 0):
            print(f"{iCnt}")

############################################################################################
##
##  This is entry point of function
##
############################################################################################

iValue = (int(input("Enter the number : ")))

DisplayFactor(iValue)
        