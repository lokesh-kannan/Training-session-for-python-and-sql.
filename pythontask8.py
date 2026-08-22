# Read and display the complete file content using read().
file = open("files/student.txt", "r")

content = file.read()

print(content)

file.close()

# Read the file line by line using readline().
file = open("files/student.txt", "r")

content = file.readline()
print(content)
content1 = file.readline()
print(content1)
content2 = file.readline()
print(content2)

file.close()

# Read all lines using readlines().

file = open("files/student.txt", "r")

lines = file.readlines()
print(lines)

file.close()

# Use tell() to display the current file pointer position.

file = open("files/student.txt", "r")

tell = file.tell()
print(tell)

file.close()

# Use seek() to move the file pointer and read the content again.

file = open("files/student.txt", "r")

print(file.read(10))

print("Position:", file.tell())

file.seek(0)

print("Position after seek:", file.tell())

print(file.read())

file.close()

# Append additional student information using a mode.
file = open("files/student.txt", "a")

file.write("\nStudent Name: Arun\n")
file.write("Age: 23\n")
file.write("Department: Mechanical\n")
file.write("Mark: 78\n")
file.close()

# Read and display the updated file content.
file = open("files/student.txt", "r")
content = file.read()
print(content)

file.close()

# Use the with open() statement to open and work with the file.
with open("files/student.txt", "r") as file:
    content = file.read()
    print(content)
    
# SyntaxError   
# print("Hello"

#Indendation error 
# if 10> 20:
# print("45")

# Runtime error
try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")