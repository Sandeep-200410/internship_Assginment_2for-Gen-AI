# Restaurant Bill Splitter

bill = float(input("Enter total bill amount: ₹"))
people = int(input("Enter number of people: "))
tax_percent = float(input("Enter tax percentage: "))
tip_percent = float(input("Enter tip percentage: "))

# tax calculation
tax_amount = bill * (tax_percent / 100)
after_tax = bill + tax_amount

# tip calculation
tip_amount = after_tax * (tip_percent / 100)
final_bill = after_tax + tip_amount

per_person = final_bill / people

print("\n---- BILL DETAILS ----")
print("Original Bill: ₹", round(bill,2))
print("Tax Amount: ₹", round(tax_amount,2))
print("After Tax: ₹", round(after_tax,2))
print("Tip Amount: ₹", round(tip_amount,2))
print("Final Total: ₹", round(final_bill,2))
print("Each Person Pays: ₹", round(per_person,2))