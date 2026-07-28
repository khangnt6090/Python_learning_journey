weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/P): ").strip().upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Pounds"
elif unit == "P":
    weight = weight / 2.205
    unit = "Kilograms"
else:
    print("Invalid unit. Please enter 'K' for Kilograms or 'P' for Pounds.")
    exit()

print(f"Your weight in {unit} is: {weight:.2f} {unit}")