# Problem Statement : Accept radius from user and calculate area of circle

# Step 1 : Understand the problem statement 
# Conclusion : We are going to use formula PI * R * R

# Step 2 : Algorithm
'''
    START 
        Accept the radius from user and store it into variable
        Create variable as PI and store value 3.14 in it
        Calculate area as PI * R * R
        Display the value of are to the user
    STOP
'''

##################################################################################################
##
##  Function Name : displayArea
##  Description :   This function is used to calculate area of circle by taking radius from user 
##  Input :         float
##  Output :        float 
##  Author :        Ajay Yogesh Varma
##  Date :          7-10-2023
##
##################################################################################################
import math

PI = math.pi

def displayArea(dRad):
    fCalculateArea = 0.0
    fCalculateArea = PI * dRad * dRad
    return fCalculateArea

#############################################################################################
##
##  This is entry point of program
##
#############################################################################################

fRadius = 0.0
fArea = 0.0

fRadius = (float(input("Enter the radius of circle : ")))

fArea = displayArea(fRadius)

print(f"Area of Circle {fArea}")