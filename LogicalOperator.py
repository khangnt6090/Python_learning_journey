#Câu điều kiện and, or, not
#and: tất cả các điều kiện phải đúng thì mới thực hiện câu lệnh
#or: chỉ cần 1 điều kiện đúng thì câu lệnh sẽ được thực hiện
#not: phủ định điều kiện, nếu điều kiện đúng thì câu lệnh sẽ không được thực hiện, nếu điều kiện sai thì câu lệnh sẽ được thực hiện

temp = 40
sunny = True

if temp <=  0 or temp >= 30:
    print("The temperature is not bad")
else:
    print("The temperature is good")

if not sunny:
    print("It is not sunny today")
else:
    print("It is sunny today")