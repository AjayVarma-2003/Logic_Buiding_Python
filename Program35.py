## Problem Statement : take a integer as a input from user and return the addition of its factors

## Conclusion : We will find the factors of number and then simply add them and return the sum

## Algorithm :

'''
    START 
        Take a integer as input and store it in variable
        iterate the for loop till the input variable to find factors
        if input variable is fully divisible by number return it as factor
        add that factors into result variable
        return the sum
    STOP
'''

############################################################################################
##
##  Function Name : SumFactors
##  Description :   Takes integer as input and returns the sum of its factors
##  Input :         Integer
##  Output :        Integer
##  Author :        Ajay Yogesh Varma
##  Date :          14-10-2023
##
############################################################################################

def SumFactors(iNo):
    iSum = 0
    for iCnt in range(1, iNo):
        if(iNo % iCnt == 0):
            iSum += iCnt

    return iSum

############################################################################################
##
##  This is entry point of function
##
############################################################################################

iValue = (int (input ("Enter the number : ")))

iRet = SumFactors(iValue)

print(f"Sum of the factors of given number is {iRet}")