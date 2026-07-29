a = 40
b = 6

# Addition
c=a+b
print("Addition of a+b: "+str(c))

# subtraction
d=a-b
print("subtraction of a-b: "+str(d))

# Multiplication
e=a*b
print("Multiplication of a*b: "+str(e))

#division
f=a/b
print("division of a/b: "+str(f))

#floor div
g=a//b
print("floor div of a//b: "+str(g))

#Modules
h=a%b
print("Modules of a mod b: "+str(h))

#Exponent
i = a**b
print("Exponent of a**b: "+str(i))

# comparison operator

print ("The comparison of a==b: "+str(a==b))

print ("The comparison of a!=b: "+str(a!=b))

print ("The comparison of a<b: "+str(a<b))

print ("The comparison of a>b: "+str(a>b))

print ("The comparison of a>=b: "+str(a>=b))

print ("The comparison of a<=b: "+str(a<=b))

#logical Operators

x=True
y=False

print(x and y)

print(x or y)

print (not x)

print(not y)

#Assigment operator

num = 25

num+=5
print (num)

num-=3
print (num)

num*=2
print(num)

num/=4
print(num)

num//=2
print(num)

num%=5
print(num)

num**=2
print(num)

#bitwise operator

a=12
b=5
#and
print (a&b)
#or
print(a|b)

print(a^b)
#not
print(~a)
#left shift
print(a<<2)
#right shift
print(a>>1)

print(" a=12 "+" Binary representation of a: "+bin(a))

print(" b=5 "+" Binary representation of b: "+bin(b))

'''
90 - 100 --> O 
80 - 89 --> A+ 
70 - 79 --> A 
60 - 69 --> B 
50 - 59 --> C 
0 - 49 --> Fail
marks = print("Enter the marks: "+str(input()))
if marks > 90 or marks < 100 :
    print("the student has obtained a 'O' grade!!!")
elif marks > 80 or marks < 89 :
    print("the student has obtained a 'A+' grade!!!")
elif marks > 70 or marks < 79 :
    print("the student has obtained a 'A' grade!!!")
elif marks > 60 or marks < 69 :
    print("the student has obtained a 'B' grade!!!") 
elif marks > 50 or marks < 59 :
    print("the student has obtained a 'C' grade!!!")
elif marks< 49:
    print("the student has failed")
else :
    print("invalid marks")'''
  
 