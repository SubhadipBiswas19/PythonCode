"""
Build a custom calculator that performs arithmetic and logical operations.
Tasks:
Define a function that takes two numbers and an operation (as a string) using *args and **kwargs to accept optional parameters like rounding precision.
Implement support for +, -, *, /, and comparison operators (==, <, >) inside the function.
Use exception handling for division by zero and invalid operations.
Demonstrate use of logical operators to combine results (e.g., check if both conditions hold).
Use raise to throw a custom exception when an unsupported operation is requested.
Use string slicing and concatenation to format the output message.
Preconditions:
Inputs: two numbers (int or float)
Operation: one of ['+', '-', '*', '/', '==', '<', '>']
Optional kwargs: round_digits (int, ≥ 0) to round the result
Division by zero must raise an exception
Unsupported operations raise custom exception
"""
class UnsupportedOperationException(Exception):
    pass

def custom_calculator(*args, **kwargs):
    if len(args) != 3:
        raise ValueError('Exactly three arguments required: number1, number2, and operation')

    num1, num2, operation = args
    round_digits = kwargs.get('round_digits', None)

    if not isinstance(num1,(int, float)) or not isinstance(num2,(int, float)):
        raise ValueError('Inputs must be integers or floats')

    try:
        result = None

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 ==0:
                raise ZeroDivisionError("Division by zero is not allowed")
            result = num1 / num2
        elif operation == '==':
            result = num1 == num2
        elif operation == '<':
            result = num1 < num2
        elif operation == '>':
            result = num1 > num2
        else:
            raise UnsupportedOperationException(f"Operation '{operation}' is not supported")

        if isinstance(result,float) and isinstance(round_digits,int) and round_digits >= 0:
            result = round(result, round_digits)

        op_str = f"{str(num1)}{operation[:1]}{str(num2)}"
        output = "Result " + op_str + " = " + str(result)
        return (output)

    except ZeroDivisionError as e:
        return f"Error: {str(e)}"
    except UnsupportedOperationException as uoe:
        return f"Error: {str(uoe)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

print(custom_calculator(10, 5, '+'))
print(custom_calculator(20, 5, '-'))
print(custom_calculator(1.25, 1.25, '*', round_digits=2))
print(custom_calculator(7, 0, '/'))
print(custom_calculator(8, 8, '=='))
print(custom_calculator(9, 3, 'mod'))