def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num1 != 0:
            return num1 / num2
        else:
            return "cannot divide by 0"
    else:
        return "error"
