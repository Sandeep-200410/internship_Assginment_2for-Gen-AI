num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not defined for negative numbers")

else:
    fact = 1
    pcs = ""
    for i in range(num, 0, -1):
        fact *= i
        pcs += str(i) + " x "

    pcs = pcs[:-3]
    print(f"{num}! = {pcs} = {fact}")