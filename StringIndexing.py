# indexing = [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[-1]) # là ký tự cuối cùng
# print(credit_number[::-1]) # đảo ngược chuỗi

last_digits = credit_number[-4:] # lấy 4 ký tự cuối cùng
print(f"XXX-XXXX-XXXX-{last_digits}") # In ra số thẻ tín dụng với 4 ký tự cuối cùng được hiển thị
