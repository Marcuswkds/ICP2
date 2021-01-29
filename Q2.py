#Q2
nonNegativeNumber = int(input("Enter a number: ")) #Getting user input for a number.
noOfSteps = 0 #Initial number of steps.

def reduceToZero(num): #Function to reduce number to zero.
    if num == 0:
        return

    if num % 2 == 0: #If number entered is divisible by 2, it is even.
        num /= 2 #If number is even, it is divided by 2.
    else:
        num -= 1 #If number is not even, it is odd. Therefore it is subtracted by 1.

    global noOfSteps
    noOfSteps += 1 #The number of steps increases by one through every loop.
    reduceToZero(num)

reduceToZero(nonNegativeNumber) #Uses the non-negative number entered by the user in the function.
print(noOfSteps) #Prints number of steps to the user.