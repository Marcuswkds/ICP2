import math
#Q1
feetHeights = [] #Creates an empty list
cmHeights = list()
n = int(input("Enter the number of students: ")) #Getting user input for the number of students

for i in range(0,n):
    ele = float(input("Enter the height of each student: "))#Getting user input for the height of each student as a float.
    cmHeight = ele * 30.48 #Formula for converting each student height entered from feet to centimetres.
    feetHeights.append(ele)
    cmHeights.append(math.floor(cmHeight * 10) / 10) #Store floor of single decimal

print(feetHeights) #Prints the list of students height in feet to the user.
print(cmHeights) #Prints the list of students height in cm to the user.

