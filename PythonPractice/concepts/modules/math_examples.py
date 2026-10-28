# math module
# The math module provides mathematical functions and constants.
# It is built into Python, so no installation is needed.
# Most functions in math work on int or float values and always return a float
# (except factorial and gcd, which return an int).

import math

# Constants
# math.pi and math.e are fixed float values stored by the module.
print(math.pi)    # 3.141592653589793 (ratio of a circle's circumference to its diameter)
print(math.e)     # 2.718281828459045 (base of the natural logarithm)

# Square root and powers
# math.sqrt() only accepts non-negative numbers; a negative value raises ValueError.
print(math.sqrt(16))     # 4.0
# math.pow(x, y) computes x raised to the power y and always returns a float.
# The ** operator is also available, but it returns an int when both inputs are ints.
print(math.pow(2, 3))    # 8.0 (always returns a float)

# Rounding
# floor() rounds toward negative infinity, ceil() rounds toward positive infinity.
# Both return an int in Python 3.
print(math.floor(4.7))   # 4  (round down)
print(math.ceil(4.2))    # 5  (round up)
print(math.floor(-4.2))  # -5 (floor goes further down for negative numbers)

# Factorial and greatest common divisor
# factorial(n) = n * (n-1) * ... * 1, and it only accepts whole numbers >= 0.
print(math.factorial(5))   # 120  (5 * 4 * 3 * 2 * 1)
# gcd finds the largest number that divides both inputs evenly.
print(math.gcd(12, 18))    # 6

# Trigonometry (angles are in radians, not degrees)
# A full circle is 2 * pi radians, which equals 360 degrees.
print(math.sin(math.pi / 2))         # 1.0 (sine of 90 degrees)
print(math.cos(0))                   # 1.0 (cosine of 0 radians)
# degrees() and radians() convert between the two units.
print(math.degrees(math.pi))         # 180.0
print(math.radians(180))             # 3.141592653589793

# Logarithms
# log(x) uses base e by default; you can pass a base as the second argument.
print(math.log(math.e))      # 1.0 (natural log)
print(math.log(8, 2))        # 3.0 (log base 2 of 8, using the optional base argument)
# log10 and log2 are shortcuts for common bases.
print(math.log10(1000))      # 3.0 (base 10)
print(math.log2(8))          # 3.0 (base 2)

# Checking special values
# Computers store floats in binary, so some decimal values are slightly off.
# That is why 0.1 + 0.2 is not exactly 0.3.
# isclose() checks whether two floats are close enough, which is the safe way to compare them.
print(math.isclose(0.1 + 0.2, 0.3))  # True (safe way to compare floats)
print(0.1 + 0.2 == 0.3)              # False (floating point error)
# nan means "not a number" (for example, the result of an invalid calculation).
print(math.isnan(float("nan")))      # True
# inf means infinity. Checking with isinf() is more reliable than comparing with ==.
print(math.isinf(float("inf")))      # True

# Using math in a real calculation: distance between two points
# hypot() gives the straight-line distance using the Pythagorean theorem.
x1, y1 = 1, 2
x2, y2 = 4, 6
distance = math.hypot(x2 - x1, y2 - y1)   # same as sqrt(dx**2 + dy**2)
print(f"Distance: {distance}")            # 5.0

# Importing only what you need
# "from math import sqrt" lets you call sqrt() directly, without the "math." prefix.
# Use this for a few functions. Importing the whole module keeps names clear, though.
from math import sqrt
print(sqrt(25))   # 5.0
