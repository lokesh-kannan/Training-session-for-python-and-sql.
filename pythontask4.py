# Write a program to print numbers from 1 to 10 using a while loop.
'''i=0
while i<10 :
    i+=1
    print(i)
    print("-----")'''

# Write a program to print even numbers between 1 and 50 using a while loop.
'''i=1
N=50
while i<=N :
    if i%2==0 :
        print("the number is :"+str(i))
        i+=1
    else :
        i+=1   ''' 

# Write a program to find the sum of numbers from 1 to 100 using a while loop.
'''i=1
n=100
sum=0
while i<=n :
    sum+=i
    i+=1;
print("the sum of numbers from 1 to 100 is "+str(sum))'''

# Write a program to display the multiplication table of a given number using a while loop.

# 4 x 1 = 4
'''
i= input("enter any number to print the table :")
n= input("enter the number which has to be multiplied :")
while i<=n or i>=n :
    mul=str(int(i)*int(n))
    print(i + " X " + n + " = " + mul)
    break'''

# Write a program to reverse a given number using a while loop
#543
#12
'''num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)
'''
# Write a program to print numbers from 1 to 20 using a for loop.

'''for i in range (1,21) :
    print (i)
'''

# Write a program to print all characters of a given string using a for loop

'''user = input("Enter the string: ")
for character in user:
    print (character)'''
    
# Write a program to print odd numbers between 1 and 50 using a for loop
'''for i in range (1,50):
    if i%2!=0:
        print(i)
     '''

