number = int(input("Enter a number to see its multiplication table: "))

for y in range(1, 11):
  # loop iterates through rows (multiplication factors)
    x = number
    z = x * y
    print("{} x {} = {}".format(x, y, z))