number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
  # loop iterates through rows (multiplication factors)
    product = number * i
    print(f"{number} x {i} = {product}")
#print()  # Move to a new line after each row
