# Commonly Used Built-in Functions in Python
# These functions are very useful in everyday programming.
# They help us work with data, strings, lists, numbers, and collections.

# 1. len() -> returns the length of a sequence
numbers = [10, 20, 30, 40]
print("len(numbers):", len(numbers))

# 2. sum() -> adds all values in an iterable
print("sum(numbers):", sum(numbers))

# 3. min() -> returns the smallest value
print("min(numbers):", min(numbers))

# 4. max() -> returns the largest value
print("max(numbers):", max(numbers))

# 5. abs() -> returns absolute value
print("abs(-15):", abs(-15))

# 6. round() -> rounds a number to nearest integer or given digits
print("round(3.14159):", round(3.14159))
print("round(3.14159, 2):", round(3.14159, 2))

# 7. type() -> tells the type of an object
name = "Python"
print("type(name):", type(name))

# 8. str() -> converts value to string
age = 25
print("str(age):", str(age))

# 9. int() -> converts value to integer
print("int('25'):", int('25'))
print("int(7.9):", int(7.9))

# 10. float() -> converts value to float
print("float('3.14'):", float('3.14'))

# 11. list() -> converts an iterable into a list
text = "hello"
print("list(text):", list(text))

# 12. tuple() -> converts an iterable into a tuple
print("tuple(numbers):", tuple(numbers))

# 13. set() -> removes duplicates and creates a set
print("set([1,2,2,3]):", set([1, 2, 2, 3]))

# 14. sorted() -> returns a sorted list
unsorted = [4, 1, 7, 2]
print("sorted(unsorted):", sorted(unsorted))

# 15. enumerate() -> gives index and value while looping
print("enumerate example:")
for index, value in enumerate(numbers):
    print(index, value)

# 16. range() -> generates a sequence of numbers
print("range example:", list(range(1, 6)))

# 17. zip() -> combines multiple iterables
names = ["A", "B", "C"]
scores = [10, 20, 30]
print("zip(names, scores):", list(zip(names, scores)))

# 18. all() -> returns True if all values are True or non-zero
print("all([1, 2, 3]):", all([1, 2, 3]))

# 19. any() -> returns True if at least one value is True or non-zero
print("any([0, 0, 1]):", any([0, 0, 1]))

# 20. bool() -> converts value to boolean
print("bool(0):", bool(0))
print("bool('hello'):", bool('hello'))

# Notes:
# These built-in functions are extremely common in Python.
# They reduce the need to write long custom logic for basic tasks.
# Learning them helps you write cleaner and faster programs.
