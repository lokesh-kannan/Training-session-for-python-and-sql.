Name = input("Enter your name: ")
# Concatination
print("--"+Name+"--")
# repetition
print(Name,Name)
# methods
# upper()
print(Name.upper())
# lower()
print(Name.lower())
# title()
print(Name.title())
# capitalize()
print(Name.capitalize())
# find()
print(Name.find("h"))
# count()
print(Name.count("L"))
# split()
print(Name.split())
# join()
print(Name.join(Name))
# isalpha()(
print(Name.isalpha())
# isdigit()
print(Name.isdigit())
# isalnum()
print(Name.isalnum())
# startswith()
print(Name.startswith("L"))
# endswith()
print(Name.endswith("K"))

# Create a string containing multiple words and use split() to separate the words.

stance = "this is a practise session where we need to get understand the topics as per the requirements and implement our code to get the relatable output so we are now applying this instead of searching the exact answers in the websites the notes is encyclopedia "
print(stance.split())

# Use join() to combine a sequence of words into a single string.
# print(stance.join(stance))
# Use find() to search for a particular substring and display the returned index.
print(stance.find("s"))
# Use count() to find how many times a character or substring occurs.
print(stance.count("e"))
# Check whether a given string:
# Contains only alphabets.
print(stance.isalpha())
# Contains only digits.
print(stance.isdigit())
# Contains alphabets and numbers.
print(stance.isalnum())

# Create variables for:
# Display all three values using an f-string.
Name = "Lokesh K"
Age = 25
City = "chennai"
print(f"Hello, Name: '{Name}' and age: '{Age}' from '{City}'!!!")