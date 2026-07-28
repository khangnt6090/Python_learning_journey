unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    unit = "Fahrenheit"
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    unit = "Celsius"
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    exit()

print(f"The temperature in {unit} is: {temp:.2f} {unit}")