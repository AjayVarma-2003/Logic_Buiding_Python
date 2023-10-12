## Problem Statement : Take percentage as input from user and print his passing criteria on screen

## Conclusion : We will use if-else condition checking for this 

## Algorithm : 
'''
    START 
        create variable value and intialize it to 0
        Take percentage as input from user and store it in value
        if - value >= 0 and < 35 then failed
        or - value >= 35 and < 50 then pass class
        or - value >= 50 and < 59 then second class
        or - value >= 59 and < 75 then first class
        or - value >= 75 and <= 100 then distinction class
    STOP
'''

#############################################################################################
##
##  Function Name : Display Class
##  Description :   Takes float as parameter and display according to float value
##  Input :         Float
##  Output :        None
##  Author :        Ajay Yogesh Varma
##  Date :          12-10-2023
##
#############################################################################################

def DisplayClass(fMarks):
    if (fMarks >= 0 and fMarks < 35.00):
        print("You are failed...")
    elif (fMarks >= 35.00 and fMarks < 50.00):
        print("You got pass class")
    elif(fMarks >= 50.00 and fMarks < 59.00):
        print("You got second class")
    elif(fMarks >= 59.00 and fMarks < 75.00):
        print("You got first class")
    elif(fMarks >= 75.00 and fMarks <= 100.00):
        print("You got distinction")
    else:
        print("Invalid marks")

#############################################################################################
##
##  This is entry point of program
##
#############################################################################################

fValue = (float(input("Enter your percentage : ")))

DisplayClass(fValue)