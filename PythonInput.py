#Basic

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello, " + name + "!")
print("You are " + str(age) + " years old.")

#Calculate the area of a rectangle

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = length * width
print("The area of the rectangle is: " + str(area) + " square units.")

#Calculate the total cost of an item
item = input("Enter the name of the item: ")
price = float(input("Enter the price of the item: "))  
quantity = int(input("Enter the quantity of the item: "))

total = price * quantity
print("The total cost of " + str(quantity) + " " + item + "(s) is: $" + str(total))
