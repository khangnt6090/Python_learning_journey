# format specifiers = {value:flags} là một cách để định dạng chuỗi trong Python, cho phép bạn kiểm soát cách hiển thị các giá trị. Dưới đây là một số ví dụ về cách sử dụng format specifiers:

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.2f}")  # Hiển thị với 2 chữ số thập phân
print(f"Price 2 is {price2: 10}") # Hiển thị với độ rộng 10 ký tự, căn phải
print(f"Price 3 is {price3:010}") # Hiển thị với độ rộng 10 ký tự, căn phải và điền số 0 vào các vị trí trống
print(f"Price 1 is {price1:>10}") # Hiển thị với độ rộng 10 ký tự, căn phải
print(f"Price 2 is {price2:<10}") # Hiển thị với độ rộng 10 ký tự, căn trái
print(f"Price 3 is {price3:^10}") # Hiển thị với độ rộng 10 ký tự, căn giữa
print(f"Price 1 is {price1:+.2f}") # Hiển thị với dấu + hoặc - và 2 chữ số thập phân
