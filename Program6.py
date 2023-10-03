# Problem Statement : Accpet two values from user and perform the addition

# Step 1: Understand problem statement
# conclusion : We have to accept two integers and perform addition

# Step 2: Write algorithm
"""START
    Accept 1st number from user and store it into no1
    Accept 2nd number from user and store it into no2
    Create one variable to store result named as ans
    Perform addition of no1 and no2 and store result into ans
    Display the result from ans to the user
   STOP
"""

# Step 3: Decide the programming language (C / C++ / Java / Python)
# We select python programming 

# Step 4: Write the program

################################################################################
#
#   Function Name :     Addition
#   Description :       It is used to perform addition of two integers
#   Input Arguments :   Integer , Integer
#   Output :            Integer
#   Author :            Ajay Yogesh Varma
#   Date :              27-09-2023
#
################################################################################

def Addition(iNo1 , iNo2):
    iSum = int(iNo1) + int(iNo2)
    return iSum

################################################################################
#
#   Following is the start of program or entry point of program where we take 
#   user inputs and then using function call we perform addition  
#
################################################################################


iValue1 = input("Enter first value : ")

iValue2 = input("Enter second value : ")

iAns = Addition(iValue1 , iValue2)

print("Sum of given number is : ", iAns)

# Step 5: Test the code 
"""
    Test Case 1:
        Input = 10 11
        Output = 21
    
    Test Case 2:
        Input = 12 -6
        Output = 6
        
    Test Case 3:
        Input = 10 0
        Output = 10
    
    Test Case 4:
        Input = -5 -6 
        Output = -11
        """