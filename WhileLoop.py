# While loop là một cấu trúc lặp trong Python, cho phép bạn thực hiện một khối mã nhiều lần miễn là điều kiện được chỉ định là True. Dưới đây là một ví dụ về cách sử dụng while loop:

#Ví dụ 1
name = input("Enter your name: ")

while name == "":
    print("Name cannot be empty. Please enter your name.")
    name = input("Enter your name: ")

print(f"Hello, {name}!")

#Ví dụ 2
age = input("Enter your age: ")

while age < 0:
    print("Age cannot be negative. Please enter a valid age.")
    age = input("Enter your age: ")

print(f"You are {age} years old.")

#Ví dụ 3
food = input("Enter your favorite food(q to quit): ")

while not food == "q":
    print(f"Your favorite food is {food}.")
    food = input("Enter your favorite food(q to quit): ")

print(f"Bye")

#Ví dụ 4
num = int(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10:
    print("Invalid number. Please enter a number between 1 and 10.")
    num = int(input("Enter a number between 1 and 10: "))
print(f"You entered {num}.")