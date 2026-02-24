print("Choose Pattern:")
print("1. Increasing Numbers")
print("2. Repeated Numbers")
print("3. Reverse Pattern")
print("4. Pyramid Pattern")

choice = int(input("Enter choice: "))
n = int(input("Enter height: "))

if choice == 1:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

elif choice == 2:
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()

elif choice == 3:
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

elif choice == 4:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        for j in range(i-1, 0, -1):
            print(j, end="")
        print()