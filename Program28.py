## Problem Statement : Print hello and the number with it that much times it is printed

## Conclusio : for example if we print 3 times then it should printed like Hello 3

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
        print(f"Hello {iCnt}")
        
############################################################################################
##
##  This is entry point of function
##
###########################################################################################

iValue = (int(input("Enter the number of times you want to display on screen : ")))

Display(iValue)