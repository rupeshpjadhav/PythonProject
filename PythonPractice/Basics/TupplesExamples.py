# Tuple Examples and Basic Methods
# A tuple is an ordered collection that is immutable.
# Once created, its contents cannot be changed.
# Tuples are useful when we want fixed data such as coordinates or records.

# -------------------------------------------------------------------
# 1. Creating tuples
# -------------------------------------------------------------------
# Tuple packing: multiple values are automatically grouped into a single tuple.
# Example: a = 10, 20, 30 is packed into a tuple automatically.
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('apple', 'banana', 'cherry')
tuple3 = (1, 'apple', 3.14, True)
print("tuple1:", tuple1)
print("tuple2:", tuple2)
print("tuple3:", tuple3)

# Another example of tuple packing.
packed = 10, 20, 30
print("Packed tuple:", packed)

# -------------------------------------------------------------------
# 2. Accessing elements
# -------------------------------------------------------------------
# Indexing starts from 0, just like lists.
print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])

# -------------------------------------------------------------------
# 3. Slicing
# -------------------------------------------------------------------
# Slicing returns a subset of the tuple.
tuple_slice = tuple1[1:4]
print("Sliced tuple1 (1:4):", tuple_slice)

# -------------------------------------------------------------------
# 4. Length of tuple
# -------------------------------------------------------------------
print("Length of tuple3:", len(tuple3))

# -------------------------------------------------------------------
# 5. Count and index methods
# -------------------------------------------------------------------
# count(value) returns how many times a value appears in the tuple.
# index(value) returns the position of the first matching value.
tuple4 = (1, 2, 2, 3, 2, 4)
print("tuple4:", tuple4)
print("Count of 2 in tuple4:", tuple4.count(2))
print("Index of 3 in tuple4:", tuple4.index(3))

# -------------------------------------------------------------------
# 6. Concatenation
# -------------------------------------------------------------------
# Adding two tuples creates a new tuple with all values from both tuples.
concat_tuple = tuple1 + tuple2
print("Concatenated tuple:", concat_tuple)

# -------------------------------------------------------------------
# 7. Repetition
# -------------------------------------------------------------------
# Multiplying a tuple repeats its items.
repeat_tuple = tuple2 * 2
print("Repeated tuple2:", repeat_tuple)

# -------------------------------------------------------------------
# 8. Membership test
# -------------------------------------------------------------------
print("Is 'banana' in tuple2?", 'banana' in tuple2)

# -------------------------------------------------------------------
# 9. Iterating through a tuple
# -------------------------------------------------------------------
print("Iterating through tuple1:")
for item in tuple1:
    print(item)

# -------------------------------------------------------------------
# 10. Tuple unpacking
# -------------------------------------------------------------------
# Unpacking means assigning values from a tuple into separate variables.
# The number of variables must match the number of elements in the tuple.
a, b, c, d, e = tuple1
print("Unpacked values from tuple1:", a, b, c, d, e)

# Example with different values.
name, age, city = ("Rupesh", 25, "Pune")
print("Name:", name)
print("Age:", age)
print("City:", city)

# -------------------------------------------------------------------
# 11. Nested tuples
# -------------------------------------------------------------------
# A tuple can contain other tuples.
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)
print("First element of first tuple in nested_tuple:", nested_tuple[0][0])

# -------------------------------------------------------------------
# 12. Immutable property demonstration
# -------------------------------------------------------------------
# Tuples are immutable, so we cannot modify an item after creation.
# This line would raise an error: tuple1[0] = 100
try:
    tuple1[0] = 100
except TypeError as e:
    print("Tuples are immutable:", e)

# -------------------------------------------------------------------
# 13. Packing and unpacking summary
# -------------------------------------------------------------------
# Packing example.
coords = 10, 20
print("Packed coords:", coords)

# Unpacking example.
x, y = coords
print("Unpacked coords:", x, y)

