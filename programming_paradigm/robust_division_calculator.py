def safe_divide(numerator, denominator):
    try:
        numerator_float = float(numerator)
        denominator_float = float(denominator)
        division = numerator_float / denominator_float
    except ValueError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result of the division is {division}")
