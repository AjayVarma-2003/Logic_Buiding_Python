## Problem Statement : Take a number as input and print * that much times

## Conclusion : 

## Algorithm :

'''
    START 
        Take a number as input from user
        store it in variable 
        run for loop number of times as input and print 
    STOP
'''

###########################################################################################
##
##  Function Name : Display
##  Description :   Takes a number as input and prints statement that much times
##  Input :         Integer
##  Output :        None 
##  Author :        Ajay Yogesh Varma
##  Date :          13-10-2023
##
############################################################################################

def Display(iNo):
    for iCnt in range (1, iNo+1):
        print("*")
        
############################################################################################
##
##  This is entry point of function
##
############################################################################################

iValue = (int(input("Enter the how many number of times you want to display * on screen : ")))

Display(iValue)