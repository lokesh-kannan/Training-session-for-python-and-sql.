print("Enter your first name: ")
first_name=input();
print("Enter your last name: ")
last_name=input();
print("Enter your city: ")
city=input();

#concatinate
print("'"+first_name+" "+last_name+"'")
#repeat
print(city*3)
#upper
print(first_name.upper())
print(last_name.upper())
print(city.upper())
#lower
print(first_name.lower())
print(last_name.lower())
print(city.lower())
#title
print(first_name.title())
print(last_name.title())
print(city.title())
#capitalise
print(first_name.capitalize())
print(last_name.capitalize())
print(city.capitalize())

#Sentence
sentence = "Python programming is easy to learn"

#Find the position of a word using find().
position = sentence.find("is")
print(position)
#Count the occurrence of a character using count().
count = sentence.count('o')
print(count)
#Convert the following sentence into a list using split():
words = sentence.split()
print(words)
#Create a list of words and join them into a sentence using join().
sentence = " ".join(words)
print(sentence)

'''Check and print the results of:
isalpha()
isdigit()
isalnum()
startswith()
endswith()'''

Alpha1 = "Lokesh is a brave student"
print(Alpha1.isalpha())

Digit = "1234567890"
print(Digit.isdigit())

Password = "Batman12345"
print(Password.isalnum())

Starts = "Lokesh is a full stack developer"
print(Starts.startswith("Lokesh"))
print(Starts.endswith("stack"))

#Create and print a formatted string using f""Lokesh
print(f"Hello this is '{first_name} {last_name}' from {city}!!!")