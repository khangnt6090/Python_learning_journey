# Nested loop là vòng lặp bên trong vòng lặp khác.
# outer loop:
#       inner loop:

rows = int(input("Nhập số dòng: "))
colums = int(input("Nhập số cột: "))
symbol = input("Nhập ký tự: ")

for x in range(rows):
    for y in range(1, colums + 1):
        print(symbol, end=" ") 
    print() 