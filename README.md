# ICP2
In Class Programming for Lists, Files, and For loops
Marcus Wong Ken Ji
Mwbwg@mail.umkc.edu
1/29/2021
Description of ICP: Learning how to use lists, loops, open and read through input files and store information back to the file.

#Question 1 Code
import math

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


Video Link: https://umkc.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=da9c75b0-ba29-403a-bb60-acc000578cac
