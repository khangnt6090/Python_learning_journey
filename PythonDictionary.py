capital = {"USA": "Washington, D.C.",
           "India": "New Delhi",
           "China": "Beijing",
           "Russia": "Moscow",}

# print(dir(capital))
# print(help(capital))
print(capital.get("USA"))

if capital.get("USA"):
    print("That capital is exists")
else:
    print("That capital is not exists")

capital.update({"Germany": "Berlin"})

print(capital)
capital.pop("Russia") # là một phương thức xóa một phần tử khỏi từ điển theo key
capital.popitem() # là một phương thức xóa một phần tử khỏi từ điển theo cặp key-value
capital.clear() # là một phương thức xóa tất cả các phần tử khỏi từ điển

for key in capital.keys():
    print(key)

values = capital.values()
print(values)   

for values in capital.values():
    print(values)

items = capital.items()
print(items)

for key, value in capital.items():
    print(key, value)

