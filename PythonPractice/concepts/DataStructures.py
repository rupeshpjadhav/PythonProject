# Data Structures in Python
# Python provides several built-in data structures for storing and organizing information.
# The most common ones are: list, tuple, dictionary, and set.
# Each one has different rules about order, mutability, and duplicates.

# List
# A list is an ordered and mutable collection.
# It allows duplicate values and is written inside square brackets [].
# fruits = ["apple", "banana", "cherry", "apple"]
# print(fruits[0])
# fruits.append("orange")
# fruits.remove("banana")
# for fruit in fruits:
#     print(f"I love {fruit}")

# Tuple
# A tuple is ordered and immutable.
# It cannot be changed once created, and it is written with parentheses ().
# colors = ("red", "green", "blue")
# print(colors[0])
# for color in colors:
#     print(color)
# my_tuple = (1, 3, 7, 8, 5, 4, 6, 8, 5)
# print(my_tuple.count(8))
# print(my_tuple.index(5))

# Dictionary
# A dictionary stores data as key-value pairs.
# It is ordered in modern Python and is written with curly braces {}.
# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# print(person["name"])
# person["age"] = 26
# person["profession"] = "Engineer"
# for key, value in person.items():
#     print(f"{key}: {value}")
# print(person.get("age"))
# person.pop("age")
# person.update({"salary": 10000})

# Set
# A set stores unique values and is unordered.
# It is useful for removing duplicates and set operations.
# numbers = {1, 2, 3, 3, 4}
# print(numbers)
# numbers.add(5)
# numbers.remove(1)
# print(numbers.intersection({2, 4, 6}))
# print(numbers.union({2, 4, 6}))

# Example usage in this file.
numbers = {1, 2, 3, 4}
for x in numbers:
    print(x)


