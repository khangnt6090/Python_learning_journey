email = input("Enter your email address: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]
#Có thể thay thế index thành email.index("@") để tìm vị trí của ký tự "@" trong chuỗi email. Nhưng phải xoá dòng 3

print(f"Your username is {username} and your domain is {domain}")