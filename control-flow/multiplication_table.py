number = int(input("Enter a number to see its multiplication table: "))

  # loop iterates through rows (multiplication factors)
for y in range(1, 11):
    print(f"{number} x {y} = {number * y}")