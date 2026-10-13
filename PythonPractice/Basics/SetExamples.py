# Set Examples and Basic Methods
# A set is an unordered collection of unique items.
# It is useful when we need to remove duplicates or perform set math like union and intersection.
# Sets are mutable, but their elements must be immutable types such as strings, numbers, or tuples.

# Example of creating a set.
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# add() inserts a new element.
my_set.add(6)
print("Set after adding 6:", my_set)

# remove() deletes a specific element.
my_set.remove(2)
print("Set after removing 2:", my_set)

# Membership test: checking whether a value exists in the set.
print("Is 3 in the set?", 3 in my_set)

# Set operations: union, intersection, and difference.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union of set_a and set_b:", set_a | set_b)
print("Intersection of set_a and set_b:", set_a & set_b)
print("Difference of set_a and set_b:", set_a - set_b)

# Iterating through a set.
print("Iterating through my_set:")
for item in my_set:
    print(item)

# Converting a list to a set removes duplicates automatically.
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set_from_list = set(my_list)
print("Set created from list to remove duplicates:", my_set_from_list)

# issubset() and issuperset() check relationships between sets.
set_c = {1, 2}
print("Is set_c a subset of my_set?", set_c.issubset(my_set))
print("Is my_set a superset of set_c?", my_set.issuperset(set_c))

# clear() removes all items from the set.
my_set.clear()
print("Set after clearing:", my_set)

# copy() duplicates the set.
my_set_copy = my_set_from_list.copy()
print("Copied set:", my_set_copy)

# Set comprehension creates a set using a compact expression.
squared_set = {x**2 for x in my_set_from_list}
print("Set comprehension (squared values):", squared_set)

# frozenset() creates an immutable set.
frozen_set = frozenset(my_set_from_list)
print("Frozen set:", frozen_set)

# A frozen set can still be used in subset checks.
print("Is frozen_set a subset of my_set_from_list?", frozen_set.issubset(my_set_from_list))

# Converting a set to a list.
set_to_list = list(my_set_from_list)
print("List created from set:", set_to_list)

# len() tells us how many items are in the set.
print("Length of my_set_from_list:", len(my_set_from_list))

# pop() removes and returns an arbitrary element from the set.
popped_element = my_set_from_list.pop()
print("Popped element:", popped_element)

