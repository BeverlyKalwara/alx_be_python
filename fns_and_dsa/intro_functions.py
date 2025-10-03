#Simple Function
# def greet():
#    print("Hello, welcome to Python!")

#greet()

#Simple function with One Parameter
def greet(name): #or greet(name="Guest") for a default parameter
    """Prints a greeting message."""
    print(f"Hello, {name}!")

greet("Lwanda")

#Simple function with Multiple Parameters
def add_numbers(a, b):
    sum1 = a + b
    print(f"The sum is {sum1}")
add_numbers(5, 3)

#function with return values
def multiply(x, y):
    return x * y

result = multiply(4, 6) # Passing argument
print("Result:", result)

#Print a Word Many Times
def repeat_word(word, times):
    for i in range(times):
        print(word)

repeat_word("Python", 3)

#Using Lambda function
add = lambda x,y: x+y
result = add(5,3)
print(result)

count = 0  # Global variable
def increment():
     count += 1  # This refers to the local count within the function
     increment()
print(count)  # Output: 0 (Global count remains unchanged)

count = 0
def increment_global():
    global count
    count += 1
increment_global()
print(count)  # Output: 1 (Global count is modified)

def outer_function():
    x = 10  # Variable in the enclosing function

    def inner_function():
        nonlocal x  # Using nonlocal to modify x from the enclosing function
        x += 5  # Modifying the value of x

    inner_function()  # Calling the nested function
    print("Modified value of x from inner function:", x)
outer_function()

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()