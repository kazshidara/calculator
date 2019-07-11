"""Math functions for calculator."""


def add(nums):
    """Return the sum of the two inputs."""
    sum = 0
    for num in nums:
        sum += num
    return sum


def subtract(nums):
    """Return the second number subtracted from the first."""
    difference = nums[0]
    for index, num in enumerate(nums):
        if index == 0:
            difference = difference
        else:
            difference -= num
    return difference

    # difference = nums[0]
    # for num in nums:
    #     difference -= num
    # difference += nums[0]
    # return difference

def multiply(nums):
    """Multiply the two inputs together."""
    product = 1

    for num in nums:
        product *= num

    return product

def divide(nums):
    """Divide the first input by the second and return the result."""
    quotient = nums[0] ** 2
    for num in nums:
        quotient /= num
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