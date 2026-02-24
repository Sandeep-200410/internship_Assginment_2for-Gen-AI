# Sum, Average, Maximum and Minimum Calcs

count = int(input("Enter how many vs you want to input: "))

total_sum = 0
largest = None
smallest = None

for index in range(1, count + 1):
    v = float(input("Enter v " + str(index) + ": "))

    # add to sum
    total_sum += v

    # check maximum
    if largest is None or v > largest:
        largest = v

    # check minimum
    if smallest is None or v < smallest:
        smallest = v

# calcs average
average_v = total_sum / count

print("\n---- RESULT ----")
print("Total Sum =", total_sum)
print("Average =", average_v)
print("Highest v =", largest)
print("Lowest v =", smallest)