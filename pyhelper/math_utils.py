
import math


def percentage(value, total):
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (value / total) * 100


def factorial(number):
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Number must be an integer")
    if number < 0:
        raise ValueError("Number cannot be negative")
    return math.factorial(number)


def is_prime(number):
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Number must be an integer")
    if number < 2:
        return False

    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False

    return True


def average(numbers):
    numbers = list(numbers)

    if not numbers:
        raise ValueError("List cannot be empty")

    return sum(numbers) / len(numbers)


def gcd(a, b):
    return math.gcd(a, b)


def lcm(a, b):
    return math.lcm(a, b)
