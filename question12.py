num = int(input("Enter number: "))
lost = int(input("Enter range: "))

print("Multiplication Table of =", num)
for i in range(1, lost+1):
    print(num, "x", i, "=", num*i)