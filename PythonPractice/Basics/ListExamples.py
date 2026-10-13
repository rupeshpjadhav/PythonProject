# List Examples and Basic Methods
# A list is an ordered, mutable collection in Python.
# It is defined using square brackets [] and can store values of different types.
# Lists are useful when we need to keep data in a sequence and change it later.

movies = ['LOTR1', 'LO2', 'LOTR3', 'LOTR4', 'LOTR5']
print("Movies in the list:", movies)

# Replacing an item at a specific index.
movies[1] = "LOTR2"
print("Updated movie list:", movies)

# sort() arranges the list in ascending or descending order.
movies.sort(reverse=True)
print("Sorted movie list (descending):", movies)

# reverse() changes the order of the list in place.
movies.reverse()
print("Reversed movie list:", movies)

# index() finds the position of a value in the list.
print("Index of 'LOTR3':", movies.index('LOTR3'))

# remove() deletes the first matching value.
movies.remove('LOTR4')
print("List after removing 'LOTR4':", movies)

# pop() removes an item from a given position.
movies.pop(0)
print("List after popping first element:", movies)

# copy() duplicates the list without affecting the original.
movies_copy = movies.copy()
print("Copied movie list:", movies_copy)

# clear() removes everything in the list.
movies.clear()
print("List after clearing:", movies)
print("Copied movie list after clearing original:", movies_copy)

# A new list with repeated values to demonstrate duplicates.
movies = ['LOTR1', 'LOTR2', 'LOTR3', 'LOTR2', 'LOTR1']
print("Count of 'LOTR2':", movies.count('LOTR2'))

movies2 = movies.copy()
movies2.reverse()
print("Reversed copied movie list:", movies2)

# Comparing two lists helps check whether they are equal.
if movies2 == movies:
    print("Both lists are palindrome.")
else:
    print("Both lists are not palindrome.")

print("Original list:", movies)
print("Reversed list:", movies2)

# extend() adds multiple elements to the list.
movies.extend(['LOTR6', 'LOTR7'])
print("Extended movie list:", movies)

newmovies = []
for i in range(len(movies)):
    if movies.count(movies[i]) > 1:
        print(f"Duplicate movie found: {movies[i]} at index {i}")
        if movies[i] not in newmovies:
            print(f"Appending {movies[i]} to new movies list.")
            newmovies.append(movies[i])
    else:
        print(f"Unique movie: {movies[i]} at index {i}")
        newmovies.append(movies[i])

print("New movies list after appending:", newmovies)

# Basic list operations: creating, appending, inserting, removing, membership test.
empty_list = []
print("Empty list:", empty_list)

empty_list.append('NewMovie1')
empty_list.append('NewMovie2')
print("List after appending elements:", empty_list)

empty_list.insert(1, 'InsertedMovie')
print("List after inserting at index 1:", empty_list)

empty_list.remove('NewMovie1')
print("List after removing 'NewMovie1':", empty_list)

popped = empty_list.pop(0)
print(f"Popped element: {popped}")
print("List after popping index 0:", empty_list)

print("Is 'NewMovie2' in the list?", 'NewMovie2' in empty_list)

print("Iterating through movies list:")
for movie in movies:
    print(movie)

# List comprehension is a compact way to create a list.
squared_numbers = [x**2 for x in range(5)]
print("List comprehension (squares):", squared_numbers)

# A nested list is a list containing other lists.
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested_list)
print("Accessing element [1][0]:", nested_list[1][0])

# Shallow copy means the data is duplicated at the top level.
list_a = [1, 2, 3]
list_b = list_a.copy()
list_b.append(4)
print("Original list_a:", list_a)
print("Copied and modified list_b:", list_b)

list_b.clear()
print("Cleared list_b:", list_b)
