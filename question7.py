while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 7:
        break

    temp = float(input("Enter temperature value: "))

    if choice == 1:
        print("Result:", (temp * 9/5) + 32, "°F")

    elif choice == 2:
        print("Result:", (temp - 32) * 5/9, "°C")

    elif choice == 3:
        print("Result:", temp + 273.15, "K")

    elif choice == 4:
        print("Result:", temp - 273.15, "°C")

    elif choice == 5:
        print("Result:", (temp - 32) * 5/9 + 273.15, "K")

    elif choice == 6:
        print("Result:", (temp - 273.15) * 9/5 + 32, "°F")