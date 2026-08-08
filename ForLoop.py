# for loop là một cấu trúc lặp trong lập trình, cho phép thực hiện một khối mã nhiều lần dựa trên một điều kiện hoặc một tập hợp các giá trị. Cú pháp cơ bản của for loop trong Python như sau:

for x in range(1, 11):
    print(x)

for x in reversed(range(1, 11)):
    print(x)
print("Happy New Year 2026!")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        break #Ngưng vòng lặp khi x bằng 13
    else:
        print(x)