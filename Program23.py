## Problem Statement : Take 3 numbers from user and return largest among them 

## Conclusion : We will take 3 intgers as input from user and return largest of them using if-else condition checking

## Algorithm :

'''
    START 
        create 3 variables as no1, no2, no3
        take 3 integer values as input from user and store it in those variables
        create variable result to store result of average
        if - no1 >=no2 and no>=no3 return no1
        if - no2 >= no1 and no2>=no3 return no2
        or - return no3
    STOP
'''

#############################################################################################
##
##  Function Name : Largest
##  Description :   It take three integers as input and return largest of them
##  Input :         Integer, Integer, Integer
##  Output :        Integer
##  Author :        Ajay Yogesh Varma
##  Date :          12-10-2023
##
#############################################################################################

def Largest (iNo1, iNo2, iNo3):
    if(iNo1 >= iNo2 and iNo1 >= iNo3):
        return iNo1
    elif(iNo2 > iNo1 and iNo2 > iNo3):
        return iNo2
    else:
        return iNo3
    
#############################################################################################
##
##  This is entry point of program
##
#############################################################################################

iValue1 = (int (input ("Enter the first number : ")))
iValue2 = (int (input ("Enter the second number : ")))
iValue3 = (int (input ("Enter the third number : ")))

iRet = Largest(iValue1, iValue2, iValue3)

print(f"Largest of among them is {iRet}")