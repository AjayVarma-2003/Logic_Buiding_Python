# Problem Statement : Take a marks from user and give the percentage 

# Step 1: Understanding problem statement 
# Conclusion : we will find percentage using (marks / total marks) * 100

# Step 2 : Write algorithm
'''
    START
        Accept marks as input from user into variable marks
        create variables total and percent to store total marks and percentages
        calculate percentage using formula (marks / total)*100
        return percentage as result
    STOP
'''
#############################################################################################
##
##  Function Name : CalculatePercentage
##  Description :   Takes a marks and total marks as integer and returns the percentage
##  Input :         integer, integer
##  Output :        float
##  Author Name :   Ajay Yogesh Varma
##  Date :          12-10-2023
##
#############################################################################################

def CalculatePercentage (iMarks , iTotal):
    fPercentage = 0.0
    
    if (iMarks > iTotal):
        print("Invalid marks\n")
        return fPercentage
    
    fPercentage = (float(iMarks) / float (iTotal)) * 100
    return fPercentage

#############################################################################################
##
##  This is entry point of program
##
#############################################################################################

imarks = 0
itotal = 0
fpercent = 0.0

imarks = (int(input("Enter the marks you get : ")))
itotal = (int(input("Enter the total marks : ")))

fpercent = CalculatePercentage(imarks, itotal)

print(f"You got {fpercent} percentage")