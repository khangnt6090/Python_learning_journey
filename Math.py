import math

friends = 10
# friends = friends + 1
# friends += 1
# friends = friends - 1
# friends -= 1
# friends = friends * 2
# friends *= 2
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
remainder = friends % 2
print(friends)
print(remainder)

# x y z
x = 3.14
y = -4
z = 5

#làm tròn số
result = round(x)
#trị tuyệt đối
result = abs(y)
#số mũ
result = pow(z, 2)
#số lớn nhất
result = max(x, y, z)
#số nhỏ nhất
result = min(x, y, z)
#căn bậc hai
result = math.sqrt(z)
#làm tròn lên
result = math.ceil(x)
#làm tròn xuống
result = math.floor(x)   

print(result)

#thư viện math
print(math.pi)
print(math.e)

# Tính chu vi hình tròn
radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

print("The circumference of the circle is: " + str(circumference) + " units.")

# Tính cạnh huyền của tam giác vuông
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse is: " + str(c) + " units.")
