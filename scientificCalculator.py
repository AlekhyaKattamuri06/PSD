import math

def sin(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a numeric value.")
    return math.sin(math.radians(x))

def cos(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a numeric value.")
    return math.cos(math.radians(x))

def tan(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a numeric value.")
    if x % 180 == 90:
        raise ValueError("Tan function is undefined for odd multiples of 90 degrees.")
    return math.tan(math.radians(x))

def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a numeric value.")
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)

def log(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a numeric value.")
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(x)

def exp(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a numeric value.")
    return math.exp(x)
