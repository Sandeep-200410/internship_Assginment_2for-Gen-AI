age = int(input("Enter age: "))
day = input("Enter day of week: ").lower()
tickets = int(input("Number of tickets: "))

# base price
if age < 3:
    price = 0
elif age <= 12:
    price = 150
elif age <= 59:
    price = 300
else:
    price = 200

base_total = price * tickets

# discount
if day in ["friday","saturday","sunday"]:
    discount = base_total * 0.20
else:
    discount = 0

final_amount = base_total - discount

print("\n--- TICKET BILL ---")
print("Base Amount: ₹", base_total)
print("Discount: ₹", discount)
print("Amount to Pay: ₹", final_amount)