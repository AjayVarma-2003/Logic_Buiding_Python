## Problem Statement : Take a standard as integer input from user and print its exam timing according to it 

## Conclusion : We will use switch case here 

## Algorithm :
'''
    START
        Create variable value 
        take standard of student as input from user and store it in value
        if standard is 1 then exam at 8Am
        if standard is 2 then exam at 9Am
        if standard is 3 then exam at 10Am
        if standard is 4 then exam at 11Am
        if standard is 5 then exam at 12Am
        or print wrong standard
    STOP
'''

#############################################################################################
##
##  Function Name : DisplayExamTime 
##  Description :   Takes standard as input and display exam timing according to the standard
##  Input :         Integer
##  Output :        None
##  Author :        Ajay Yogesh Varma
##  Date :          12-10-2023
##
#############################################################################################

def DisplayExamTime (iStandard):
    match iStandard:
        case 1:
            print("Your exam is at 8 AM ")
        case 2:
            print("Your exam is at 9 AM ")
        case 3:
            print("Your exam is at 10 AM ")
        case 4:
            print("Your exam is at 11 AM ")
        case 5:
            print("Your exam is at 12 AM ")
        case _:
            print("Invalid Standard")
            
#############################################################################################
##
##  This is entry point of program
##
#############################################################################################

iValue = (int (input("Enter your standard : ")))

DisplayExamTime(iValue)