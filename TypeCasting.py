name = "Khang"
age = 20
gpa = 3.5
student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student))

age = float(age)
print(type(age))

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)

#Số miễn khác 0 sẽ là True, số 0 sẽ là False
age = bool(age)
print(age)

#Ký tự miễn có sẽ là True, ký tự rỗng sẽ là False
name = bool(name)
print(name)

x = 2
y = 2.0

x = x / y
print(x)