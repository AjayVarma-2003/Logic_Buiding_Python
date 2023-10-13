## Problem Statement : Print Jay Ganesh on screen 5 times

## Conclusion : We have to print Jay Ganesh 5 times on screen

###########################################################################################
##
##  Function Name : Display
##  Description :   Prints 5 strings on screen
##  Input :         Integer
##  Output :        None 
##  Author :        Ajay Yogesh Varma
##  Date :          13-10-2023
##
############################################################################################

def Display(iNo):
    iCnt = 0
    
    for iCnt in range(0, iNo):
        print("Jay Ganesh...")
        

############################################################################################
##
##  This is entry point of function
##
###########################################################################################

iValue = (int (input("Enter how many times you want to display : ")))

Display(iValue)