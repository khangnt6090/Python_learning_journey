# list = [] là một danh sách rỗng
# set = {} là một tập hợp rỗng
# tuple = () là một bộ rỗng

fruits = ["apple", "banana", "cherry"] # nếu sửa [] thành () hay {} thì kết quả in ra sẽ nằm trong ngoặc đó

print(fruits) # Output: ['apple', 'banana', 'cherry']
# print(fruits[0]) # Output: apple
# print(pineapple in fruits) # Output: False
fruits.append("pineapple") # thêm pineapple vào danh sách fruits
fruits.remove("banana") # xóa banana khỏi danh sách fruits
fruits.insert(1, "orange") # thêm orange vào vị trí thứ 1 trong danh sách fruits
fruits.sort() # sắp xếp danh sách fruits theo thứ tự bảng chữ cái
fruits.reverse() # đảo ngược danh sách fruits
fruits.clear() # xóa tất cả các phần tử trong danh sách fruits

for x in fruits:
    print(x) # Output: apple, banana, cherry