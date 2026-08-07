'''student = ["lokesh", "Pushkar", "dinakar", "jayanth", "vignesh", "suresh", "mukesh", "gopal", "vicky", "rakesh"]
print(student)
student.append(120)
student.insert(2,"gokul")
print(student)
teacher = ["livin",100]
student.extend(teacher)
print(student)
student.remove(120)
print(student)
student.pop()
print(student)
student.pop(3)
print(student)
print(student.index("livin"))
print(student.count("lokesh"))
student.reverse()
print(student)
student.sort()
print(student)'''

#tuple 
detail = ("Lokesh", 24, "Developer", "cehnnai", 80)
print(detail)
print(detail.index(24))
print(detail.count("Lokesh"))
detail1 = ("Lokesh", 24, "Developer", "cehnnai", 80, "Lokesh", 24, "Developer", "cehnnai", 80)
print(detail1.count("Lokesh"))
for i in range(len(detail1)):
    print(detail1[i])