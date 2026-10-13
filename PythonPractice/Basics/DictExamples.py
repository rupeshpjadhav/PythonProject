# Dictionary Examples and Basic Methods
# A dictionary stores data in key-value pairs.
# It is useful when you want to access data by a meaningful name instead of by index.
# Example: person['name'] gets the value for the key 'name'.
# Dictionaries are mutable, which means we can add, update, or remove items.

my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Accessing values using keys.
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Adding a new key-value pair.
my_dict['email'] = 'alice@example.com'
print("Updated dictionary:", my_dict)

# Updating an existing value.
my_dict['age'] = 31
print("Updated dictionary:", my_dict)

# Removing a key-value pair.
del my_dict['city']
print("Dictionary after removing 'city':", my_dict)

# Checking whether a key exists before using it.
if 'email' in my_dict:
    print("Email:", my_dict['email'])
else:
    print("Email key not found.")

# Iterating through dictionary items.
print("\n--- Iterating through dictionary ---")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Getting keys and values as lists.
keys = list(my_dict.keys())
values = list(my_dict.values())
print("Keys:", keys)
print("Values:", values)

# The len() function gives the number of key-value pairs in the dictionary.
print("Length of dictionary:", len(my_dict))

# Clearing a dictionary removes all entries.
my_dict.clear()
print("Dictionary after clearing:", my_dict)

# copy() creates a duplicate dictionary.
my_dict_copy = my_dict.copy()
print("Copied dictionary:", my_dict_copy)

# Nested dictionaries can hold another dictionary inside a dictionary.
nested_dict = {
    'person1': {'name': 'Bob', 'age': 25},
    'person2': {'name': 'Charlie', 'age': 35}
}
print("Nested dictionary:", nested_dict)
print("Person1 Name:", nested_dict['person1']['name'])
print("Person2 Age:", nested_dict['person2']['age'])

# Dictionary comprehension creates a dictionary in one line.
squared_dict = {x: x**2 for x in range(5)}
print("Squared dictionary:", squared_dict)

# Merging dictionaries using unpacking.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

# get() returns a default value if the key is not found.
print("Get 'a' from merged_dict:", merged_dict.get('a', 'Key not found'))

# setdefault() inserts a key with a default value only if it does not already exist.
print("Get 'd' from merged_dict with setdefault:", merged_dict.setdefault('d', 4))
print("Merged dictionary after setdefault:", merged_dict)

# pop() removes and returns a specific key-value pair.
popped_value = merged_dict.pop('b', 'Key not found')
print("Popped value:", popped_value)
print("Merged dictionary after pop:", merged_dict)

# popitem() removes the last inserted item.
popped_item = merged_dict.popitem()
print("Popped item:", popped_item)
print("Merged dictionary after popitem:", merged_dict)

# update() adds or changes items from another dictionary.
update_dict = {'e': 5, 'f': 6}
merged_dict.update(update_dict)
print("Merged dictionary after update:", merged_dict)

# fromkeys() creates a new dictionary with the same default value for each key.
keys = ['x', 'y', 'z']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print("New dictionary created with fromkeys:", new_dict)

# A dictionary can be iterated item by item.
items = merged_dict.items()
print("Items in merged_dict:")
for key, value in items:
    print(f"{key}: {value}")

# keys() returns all dictionary keys.
keys = merged_dict.keys()
print("Keys in merged_dict:")
for key in keys:
    print(key)

# values() returns all dictionary values.
values = merged_dict.values()
print("Values in merged_dict:")
for value in values:
    print(value)

# Functions can accept dictionaries as arguments.
def get_person_info(person_dict, key):
    return person_dict.get(key, 'Key not found')

person_info = {'name': 'David', 'age': 28, 'city': 'Los Angeles'}
print("Person Info:", get_person_info(person_info, 'name'))
print("Person Info:", get_person_info(person_info, 'country'))

# Default values can help avoid KeyError when a key is missing.
default_dict = {'name': 'Unknown', 'age': 0, 'city': 'Unknown'}


def get_default_info(info_dict, key):
    return info_dict.get(key, 'Default Value')

print("Default Name:", get_default_info(default_dict, 'name'))
print("Default Country:", get_default_info(default_dict, 'country'))

# Nested functions can also use dictionaries.
def outer_function():
    inner_dict = {'x': 10, 'y': 20}

    def inner_function(key):
        return inner_dict.get(key, 'Key not found')

    print("Inner Function - x:", inner_function('x'))
    print("Inner Function - z:", inner_function('z'))

outer_function()

# List comprehension can create a dictionary from a list.
numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x**2 for x in numbers}
print("Squared Dictionary:", squared_dict)

# Conditional logic can also be used while building a dictionary.
def categorize_number(num):
    if num < 0:
        return 'Negative'
    elif num == 0:
        return 'Zero'
    else:
        return 'Positive'

number_dict = {x: categorize_number(x) for x in range(-2, 3)}
print("Number Categorization Dictionary:", number_dict)

# Sorting a dictionary by value is possible with sorted().
sorted_dict = dict(sorted(squared_dict.items(), key=lambda item: item[1]))
print("Sorted Dictionary:", sorted_dict)

# JSON is a common format for storing dictionaries as text.
import json

json_string = json.dumps(merged_dict)
print("JSON String:", json_string)

dict_from_json = json.loads(json_string)
print("Dictionary from JSON:", dict_from_json)

# try/except helps handle missing keys safely.
try:
    value = merged_dict['non_existent_key']
except KeyError:
    value = 'Key not found'
print("Value:", value)


def safe_get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return 'Key not found'

print("Safe Get Value:", safe_get_value(merged_dict, 'a'))
print("Safe Get Value:", safe_get_value(merged_dict, 'non_existent_key'))


