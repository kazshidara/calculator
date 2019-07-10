"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    sum = num1 + num2
    return sum


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    difference = num1 - num2
    return difference


def multiply(num1, num2):
    """Multiply the two inputs together."""
    product = num1 * num2
    return product

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    quotient = num1/num2
    return quotient

def square(num1):
    """Return the square of the input."""
    squared = num1 **2
    return squared

def cube(num1):
    """Return the cube of the input."""
    cubed = num1 ** 3
    return cubed


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    exponentiated = num1 ** num2
    return exponentiated

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    remainder = num1 % num2
    return remainder

def add_mult(num1, num2, num3):
    """Return the product of num3 and the sum of num1 and num2"""
    product = (num1 + num2) * num3
    return product

def add_cubes(num1, num2):
    """Return the sum of the cubes of num1 and num2"""
    sum = cube(num1) + cube(num2)
    return sum
