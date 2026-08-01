#Ví dụ 1

# name = input("Enter your full name: ")

# result = len(name)
# result = name.find("K")  # tìm vị trí của chữ cái "K" trong chuỗi name. Nếu không tìm thấy, nó sẽ trả về -1
# result = name.rfind("K")  # tìm vị trí cuối cùng của chữ cái "K" trong chuỗi name. Nếu không tìm thấy, nó sẽ trả về -1
# result = name.capitalize()  # viết hoa chữ cái đầu tiên của chuỗi name và các chữ cái còn lại sẽ được viết thường
# result = name.upper()  # chuyển tất cả các chữ cái trong chuỗi name thành chữ hoa
# result = name.lower()  # chuyển tất cả các chữ cái trong chuỗi name thành chữ thường
# result = name.isdigit()  # kiểm tra xem chuỗi name có phải là một số hay không. Nếu đúng, nó sẽ trả về True, ngược lại trả về False
# result = name.isalpha()  # kiểm tra xem chuỗi name có phải là một chuỗi chỉ chứa các chữ cái hay không. Nếu đúng, nó sẽ trả về True, ngược lại trả về False
# result = name.replace(" ", "_")  # thay thế tất cả các khoảng trắng trong chuỗi name bằng dấu gạch dưới "_"

# print(result)

#Ví dụ 2: Bài tập kiểm tra input của user
# Tên không được quá 12 ký tự
# Tên không được có khoảng trắng
# Tên không được có số

username = input("Enter your username: ")

if len(username) > 12:
    print("Tên không được quá 12 ký tự")
elif not username.find(" ") == -1:
    print("Tên không được có khoảng trắng")
elif not username.isalpha():
    print("Tên không được có số")
else:
    print("Xin chào, " + username)

