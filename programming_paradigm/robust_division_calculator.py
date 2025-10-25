def safe_divide(numerator, denominator):
    ##Safely divide two numbers and handle common errors.
    try:
        # Try converting inputs to numbers
        num = float(numerator)
        den = float(denominator)

        # Try performing the division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."