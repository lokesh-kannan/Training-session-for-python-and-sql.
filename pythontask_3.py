'''# If, Elif and Else
# Write a program to check whether a number is positive, negative, or zero.
num = int (input("Enter the number :"))
if num > 0:
    print("the entered number is a positive number "+ str(num))

elif num < 0:
    print("the entered number is a negative number "+ str(num))
else :
    print("the enter number is Invalid ")
    
# Write a program to check whether a number is even or odd.
num1 = int (input("Enter the number :"))
if num1%2==0:
    print("the entered number is even number "+ str(num1))
else :
    print("the entered number is odd number "+ str(num1))

# Write a program to determine whether a person is eligible to vote based on age.

Age = int (input("Enter the age :"))
if Age >= 18 :
    print("the person is eligible to vote")
else :
    print("the person is not eligible to vote")

# Write a program to find the largest among three numbers.
# Get three numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the result
print("The largest number is:", largest)



90 - 100 --> O 
80 - 89 --> A+ 
70 - 79 --> A 
60 - 69 --> B 
50 - 59 --> C 
0 - 49 --> Fail

marks = int(input("Enter the marks: "))
if marks >= 90:
    print("the student has obtained a 'O' grade!!!")
elif marks >= 80:
    print("the student has obtained a 'A+' grade!!!")
elif marks >=70:
    print("the student has obtained a 'A' grade!!!")
elif marks >= 60 :
    print("the student has obtained a 'B' grade!!!") 
elif marks > 50 :
    print("the student has obtained a 'C' grade!!!")
elif marks< 49:
    print("the student has failed")
else :
    print("invalid marks")
    
# Write a program to check whether a given year is a leap year.

# Get year from user
year = int(input("Enter a year: "))

# Check leap year condition
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")'''
    
#nested if
username = input("Enter the user name: ")
password = input("Enter the password: ")
if username == "Lokesh":
    print("The username is valid "+ username)
    if(password == "chennai@123"):
        print("you have logged in sucessfully!!!")
    else :
        print("the password is incorrect!!"+password)
else :
    print("The username is Invalid!!!")
    
#scholarships
marks = int(input("Enter the marks: "))
attendence = int(input("Enter the attendence: "))
if marks >= 70:
    print("The marks are eligible "+ str(marks))
    if(attendence >= 80):
        print("you are eligible for scholarships!!!")
    else :
        print("your attendance is low!!!"+ attendence)
else :
    print("your marks are not upto the mark!!!")
    
#campus placement
CGPA = int(input("Enter the CGPA for 10: "))
arrears = int(input("Enter the no of arrears: "))
if CGPA >= 8 :
    print("The CGPA are eligible "+ str(CGPA))
    if(arrears <= 5):
        print("you are eligible for placements!!!")
    else :
        print("your need to improve and need to clear the backlogs!!!"+ arrears)
else :
    print("your CGPA are not upto the mark!!!")