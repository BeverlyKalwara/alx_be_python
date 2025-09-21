number = int(input("Enter the size of the pattern: "))

row = 0
while row < number:
    for i in range(number):
        print("*", end="")  # Print stars on the same line
    print()  # Move to the next line after each row
    row += 1


