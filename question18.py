def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    return a/b
def modulus(a,b): return a%b
def power(a,b): return a**b

while True:
    print("\n1.Add 2.Sub 3.Mul 4.Div 5.Mod 6.Power 7.Exit")
    ch=int(input("Enter choice: "))

    if ch==7:
        break

    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))

    if ch==1: print(add(a,b))
    elif ch==2: print(subtract(a,b))
    elif ch==3: print(multiply(a,b))
    elif ch==4: print(divide(a,b))
    elif ch==5: print(modulus(a,b))
    elif ch==6: print(power(a,b))