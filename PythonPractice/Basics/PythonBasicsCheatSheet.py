# Python Basics Cheat Sheet
# This file brings together the most important Python concepts for quick revision.
# It is designed for beginners to learn the basics in one place.

# =====================================================
# 1. PYTHON DATA TYPES
# =====================================================
# int: whole numbers
age = 25
print("int example:", age)

# float: decimal numbers
price = 19.99
print("float example:", price)

# str: text
name = "Rupesh"
print("str example:", name)

# bool: True or False
is_student = True
print("bool example:", is_student)

# list: ordered and mutable
fruits = ["apple", "banana", "mango"]
print("list example:", fruits)

# tuple: ordered and immutable
point = (10, 20)
print("tuple example:", point)

# set: unique values, unordered
numbers = {1, 2, 3, 3, 4}
print("set example:", numbers)

# dict: key-value pairs
student = {"name": "Alice", "age": 21}
print("dict example:", student)

# None: no value
result = None
print("None example:", result)

# =====================================================
# 2. VARIABLES AND ASSIGNMENT
# =====================================================
# Variable names should be descriptive and follow Python naming rules.
value1 = 10
value2 = 20
sum_value = value1 + value2
print("sum:", sum_value)

# =====================================================
# 3. OPERATORS
# =====================================================
print("Arithmetic:", 10 + 5, 10 - 5, 10 * 5, 10 / 5)
print("Modulo:", 10 % 3)
print("Exponent:", 2 ** 3)
print("Comparison:", 5 > 3, 5 == 5)
print("Logical:", True and False, True or False, not True)

# =====================================================
# 4. STRING METHODS
# =====================================================
text = " python is fun "
print("upper():", text.upper())
print("lower():", text.lower())
print("strip():", text.strip())
print("split():", text.strip().split())
print("replace():", text.strip().replace("fun", "easy"))
print("find():", text.find("fun"))
print("len():", len(text))
print("slice:", text[0:6])

# =====================================================
# 5. LIST METHODS
# =====================================================
items = [3, 1, 4, 2]
items.append(5)
print("after append:", items)
items.insert(1, 10)
print("after insert:", items)
items.remove(10)
print("after remove:", items)
print("pop:", items.pop())
print("sorted:", sorted(items))
print("index:", items.index(4))
print("count:", items.count(4))

# =====================================================
# 6. TUPLE, SET, DICTIONARY
# =====================================================
# Tuple
coords = (10, 20)
print("tuple coords:", coords)

# Set
letters = {"a", "b", "a", "c"}
print("set letters:", letters)

# Dictionary
person = {"name": "John", "age": 30}
print("person name:", person["name"])
person["city"] = "Mumbai"
print("updated person:", person)

# =====================================================
# 7. CONDITIONAL STATEMENTS
# =====================================================
marks = 75
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# =====================================================
# 8. LOOPS
# =====================================================
print("For loop:")
for i in range(1, 5):
    print(i)

print("While loop:")
count = 0
while count < 3:
    print(count)
    count += 1

# =====================================================
# 9. FUNCTIONS
# =====================================================

def add(a, b):
    return a + b

print("Function result:", add(5, 7))

# =====================================================
# 10. BUILT-IN FUNCTIONS
# =====================================================
print("len([1,2,3]):", len([1, 2, 3]))
print("sum([1,2,3]):", sum([1, 2, 3]))
print("min([3,1,7]):", min([3, 1, 7]))
print("max([3,1,7]):", max([3, 1, 7]))
print("abs(-9):", abs(-9))
print("round(3.14159, 2):", round(3.14159, 2))
print("type(10):", type(10))
print("str(100):", str(100))
print("int('100'):", int('100'))
print("float('2.5'):", float('2.5'))
print("list('abc'):", list('abc'))
print("set([1,2,2]):", set([1, 2, 2]))

# =====================================================
# 11. FILE HANDLING
# =====================================================
with open("demo_file.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("This is a demo file.\n")

with open("demo_file.txt", "r") as file:
    content = file.read()
    print("File content:", content)

# =====================================================
# 12. IMPORTANT NOTES
# =====================================================
# - Lists are mutable, tuples are immutable.
# - Strings are immutable, so methods return new strings.
# - Dictionaries store data as key-value pairs.
# - Sets remove duplicates automatically.
# - Functions help reuse code.
# - Built-in functions save time and make code simpler.

# End of cheat sheet.
