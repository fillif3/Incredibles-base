'''
Arithmetic operations
'''

def summation(a, b):
    """
    Sum two numbers.

    Parameters:
    -----------
    a: float
    b: float

    Returns:
    -----------
    float, the sum of a and b
    """
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed.")
def square(a)
    return a*a

def multiplication(a, b):
    return a * b 
