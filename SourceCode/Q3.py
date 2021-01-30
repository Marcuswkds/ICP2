#Q3
import sys
text = open("myFile.txt", "r") #Opens the input file named "myFile.txt" and reads it.

d = dict() #Creates an empty dictionary

for line in text: #Loops through each line of the file.

    line = line.strip()  #Remove the leading spaces and newline character.

    line = line.lower()   #Converts all characters in line to lowercase.

    words = line.split(" ") #Splits each line into separate words.

    for word in words: #Iterates over each word in line

        if word in d: #Checks to see if the word is already in the dictionary

            d[word] = d[word] + 1 #If the word is already in the dictionary, increment the word count by 1.
        else:

            d[word] = 1 #If not, add the word to dictionary with count of 1

sys.stdout = open('myFile.txt','wt') #Opens the file named "myFile" again to write in it.
for key in list(d.keys()): # Print the contents of dictionary back to the file.
    print(key, ":", d[key])
