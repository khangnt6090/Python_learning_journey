#conditional expressions là cách viết rút gọn của câu lệnh if else trong Python. Nó cho phép bạn gán giá trị cho một biến dựa trên một điều kiện, tất cả trong một dòng duy nhất. Cú pháp cơ bản là:
# variable = value_if_true if condition else value_if_false

num = 5
a = 6
b = 7
age = 20
temperature = 30
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
status = "Adult" if age >= 18 else "Child"
weather = "Hot" if temperature > 25 else "Cold"
access_level =  "Full Access" if user_role == "admin" else "Limited Access"

print(result)
print(max_num)
print(status)
print(weather)
print(access_level)