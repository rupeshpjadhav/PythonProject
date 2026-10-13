# Python Reference: String Methods, List Methods, and Important Built-in Functions
# This file groups commonly used Python tools by category for easy learning.
# It is a quick revision guide for beginners.

# =====================================================
# 1. STRING METHODS
# =====================================================
text = "  python is fun and easy  "
print("Original text:", text)

# Case conversion
print("upper():", text.upper())
print("lower():", text.lower())
print("title():", text.title())
print("capitalize():", text.capitalize())

# Searching and replacement
print("find('fun'):", text.find('fun'))
print("replace('easy', 'simple'):", text.replace('easy', 'simple'))

# Splitting and joining
words = text.split()
print("split():", words)
print("join():", "-".join(words))

# Removing spaces
print("strip():", text.strip())
print("lstrip():", text.lstrip())
print("rstrip():", text.rstrip())

# Checking content
print("startswith('python'):", text.strip().startswith('python'))
print("endswith('easy'):", text.strip().endswith('easy'))
print("isalpha() on 'python':", 'python'.isalpha())
print("isdigit() on '123':", '123'.isdigit())
print("isalnum() on 'python123':", 'python123'.isalnum())

# String length
print("len(text):", len(text))

# Indexing and slicing
print("text[0]:", text[0])
print("text[0:6]:", text[0:6])
print("text[::-1]:", text[::-1])

# =====================================================
# 2. LIST METHODS
# =====================================================
nums = [5, 2, 8, 1, 9]
print("\nList before:", nums)

# Adding elements
nums.append(7)
print("append(7):", nums)

nums.insert(1, 10)
print("insert(1, 10):", nums)

# Removing elements
nums.remove(10)
print("remove(10):", nums)

popped = nums.pop()
print("pop():", popped, "Remaining:", nums)

# Reordering
nums.sort()
print("sort():", nums)

nums.reverse()
print("reverse():", nums)

# Searching and counting
print("index(8):", nums.index(8))
print("count(8):", nums.count(8))

# Copying and clearing
nums_copy = nums.copy()
print("copy():", nums_copy)
nums_copy.clear()
print("clear():", nums_copy)

# List length
print("len(nums):", len(nums))

# =====================================================
# 3. IMPORTANT BUILT-IN FUNCTIONS GROUPED BY CATEGORY
# =====================================================

# A. Number functions
print("\n-- Number functions --")
print("abs(-12):", abs(-12))
print("round(3.14159, 2):", round(3.14159, 2))
print("sum([1, 2, 3, 4]):", sum([1, 2, 3, 4]))
print("min([3, 1, 9, 2]):", min([3, 1, 9, 2]))
print("max([3, 1, 9, 2]):", max([3, 1, 9, 2]))

# B. Type conversion functions
print("\n-- Type conversion --")
print("int('42'):", int('42'))
print("float('3.14'):", float('3.14'))
print("str(123):", str(123))
print("list('abc'):", list('abc'))
print("tuple([1, 2, 3]):", tuple([1, 2, 3]))
print("set([1, 1, 2]):", set([1, 1, 2]))

# C. Collection helpers
print("\n-- Collection helpers --")
print("sorted([4, 1, 3]):", sorted([4, 1, 3]))
print("enumerate(['a', 'b']):", list(enumerate(['a', 'b'])))
print("zip(['A', 'B'], [1, 2]):", list(zip(['A', 'B'], [1, 2])))
print("range(5):", list(range(5)))

# D. Boolean checks
print("\n-- Boolean helpers --")
print("all([True, 1, 'python']):", all([True, 1, 'python']))
print("any([0, False, 'x']):", any([0, False, 'x']))
print("bool(0):", bool(0))
print("bool('hello'):", bool('hello'))

# E. Type inspection
print("\n-- Type inspection --")
print("type(10):", type(10))
print("type('abc'):", type('abc'))
print("type([1, 2]):", type([1, 2]))

# =====================================================
# 4. QUICK NOTES
# =====================================================
# - len() gives the length of a string/list/tuple/dictionary/set.
# - min() and max() work with numbers or comparable values.
# - sorted() returns a sorted list, without changing the original one.
# - list methods modify the list in place.
# - string methods usually return a new string and do not change the original string.
# - built-in functions help simplify code and reduce manual logic.
