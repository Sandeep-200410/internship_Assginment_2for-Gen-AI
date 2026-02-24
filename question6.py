# Grade Calculator for 5 subjects

marks = []
for i in range(1,6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

# Pass condition
passed = all(m >= 40 for m in marks)

# Grade system
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- RESULT ---")
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage,2), "%")
print("Grade:", grade)
print("Status:", "PASS" if passed else "FAIL")