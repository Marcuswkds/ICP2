# ICP2

In Class Programming for Lists, Files, and For loops

Marcus Wong Ken Ji

Mwbwg@mail.umkc.edu

1/29/2021

Description of ICP: Learning how to use lists, loops, open and read through input files and store information back to the file.

#Question 1 Code

![image](https://user-images.githubusercontent.com/72952948/106348974-d64abe00-628f-11eb-99c2-f40c3e7b7ca1.png)

I started by creating two empty lists. I then asked the user for the number students they want to enter.I then used the range function and asked the user to input the student's height in feet as float. I then used the input as elements in my lists and used the multiplied each element with 30.48 in order to convert the heights into centimetres.I then appended the and stored the floor of the resulting floats in one decimal place. Finally I printed both the lists of heights in feet and in centimetres for each student.

![image](https://user-images.githubusercontent.com/72952948/106349104-bc5dab00-6290-11eb-993c-94ca10ecb8a0.png)

#Question 2 Code

![image](https://user-images.githubusercontent.com/72952948/106349126-f4fd8480-6290-11eb-8557-8b17d28bbff1.png)

I started by getting user input for a nonnegative integer. Then, I initialized the number of steps with 0. In the reducetozero function I used for loops to determine if the number is even, divide the number by 2. If the number is odd, subtract 1 from the number. For each loop, I also incremented the number of steps till the number eventually reaches 0. I then output the number of steps it took for the number to reduce to zero to the user.

![image](https://user-images.githubusercontent.com/72952948/106349224-e6639d00-6291-11eb-93f2-e59336d6c557.png)

#Question 3 Code

![image](https://user-images.githubusercontent.com/72952948/106349243-2296fd80-6292-11eb-82d8-44bf590b9e9c.png)

For Question 3 I started by importing the sys module, and then creating an empty dictionary. I then opened a file named "myFile.txt" which I created beforehand in order to write a couple of lines in order to read through the input file. I then used a for loop in order to iterate through the lines in the input file and the line.strip() method in order to remove the leading spaces and newline character. Next, I used the line.lower() method in order to make every word lowercase and finally use the split() method in order to split each line into separate words. I then use another for loop in order to determine if the words in the lines already exist in my dictionary or not. If the word already exists in my dictionary, it will increment the word count for that word by 1. If it doesn't already exist in my dictionary, it will add it to the dictionary and increment the word count of that word by 1 as well. Finally I reopen the input file to write in it in order to print out the word counts for each word and close the file. 

Input file before running the program.

![image](https://user-images.githubusercontent.com/72952948/106349424-5888b180-6293-11eb-9c6a-9638e62c50e0.png)

Input file after running the program

![image](https://user-images.githubusercontent.com/72952948/106349448-7fdf7e80-6293-11eb-84ff-054fe7d907b5.png)



Video Link: https://umkc.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=da9c75b0-ba29-403a-bb60-acc000578cac
