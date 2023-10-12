# Problem Statement : Find cube of number by taking number from user

# Step 1 : Understand the problem statement 
# Conclusion : We will find cube by No * No * No

# Step 2 : Write the Algorithm
'''
    START 
       Accept the number from user and store it in variable No
       Create variable cube for calculating cube 
       Calculate cube of number as No * No * No
       return the cube of number
    STOP 
'''
#############################################################################################
##
##  Function Name : CalculateCube
##  Description :   Take number from user as input and returns its cube
##  Input :         integer
##  Output :        integer
##  Author :        Ajay Yogesh Varma
##  Date :          7-10-2023
##
#############################################################################################
def CalculateCube (iValue):
    iCube = 0
    iCube = iValue * iValue * iValue
    return iCube

#############################################################################################
##
##  This is entry point of program
##
#############################################################################################

iNo = 0
iAns = 0

iNo = (int(input("Enter the number : ")))

iAns = CalculateCube(iNo)

print(f"The cube of number is : {iAns}")