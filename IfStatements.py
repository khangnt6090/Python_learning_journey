#Câu điều kiện if else

#Ví dụ 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("Age cannot be negative.")
elif age >= 100:
    print("You must be less than 100 years old to sign up.")
else:
    print("You must be at least 18 years old to sign up.")

#Ví dụ 2
response = input("Do you like food? (Y/N): ")

if response.upper() == "Y":
    print("Great! Food is awesome.")
elif response.upper() == "N":
    print("Oh no! You should try some delicious food.")

#Ví dụ 3
name = input("Enter your name: ")
if name == "":
    print("You didn't enter a name.")
else:
    print("Hello, " + name + "!")

#Ví dụ 4
for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")
