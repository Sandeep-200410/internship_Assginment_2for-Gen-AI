year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
    if year % 400 == 0:
        print("Reason: divisible by 400,")
    else:
        print("Reason: divisible by 4 but not 100,")
else:
    print(year, "is not a Leap Year")
    print("Reason: not satisfying leap year conditions")