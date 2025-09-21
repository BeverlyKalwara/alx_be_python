'''
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)
'''
#loop iterates over the message string,
#assigning each character (including spaces, punctuation, and symbols) to the variable character 
# and printing it on a new line.
#message = "Hello, world!"

##for character in message:
#  print(character)

#numbers = [1, 5, 3, 9]
#total = 0

#for i in numbers:
#    sum_value = i + total
#    total = sum_value

#print(total)

#successf = False
#for number in range(3):
#    print("Attempt")
#    if successf:
#        print("Successful")
#        break
#else:
#    print("Attempted 3 times and failed")

#for i in range(1, 11):
#  # Outer loop iterates through rows (multiplication factors)
#  for j in range(1, 11):
#    # Inner loop iterates through columns (other factors)
#    product = i * j
#    print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
#  print()  # Move to a new line after each row

rows = 5

for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()  # Move to a new line after each row of asterisks