# Dunder (double-underscore) methods and operator overloading
# Dunder methods are special methods whose names start and end with __.
# Python calls them for operations such as str(obj), len(obj), and obj1 + obj2.
# Define only the behaviors that make sense for your class.


class Vector:
    def __init__(self, x, y):
        # __init__ initializes the object's state after it has been created.
        self.x = x
        self.y = y

    def __repr__(self):
        # __repr__ provides a developer-friendly representation.
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        # __str__ provides a readable representation for users.
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        # Called for vector1 + vector2.
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # Called for vector1 - vector2.
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        # Called for vector * number.
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        # Called for number * vector when the number is on the left.
        return self * scalar

    def __eq__(self, other):
        # Called for vector1 == vector2.
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y


class ShoppingCart:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        # Enables len(cart).
        return len(self.items)

    def __iter__(self):
        # Enables for item in cart.
        return iter(self.items)

    def __getitem__(self, index):
        # Enables cart[index] and slicing such as cart[0:2].
        return self.items[index]

    def __contains__(self, item):
        # Enables item in cart.
        return item in self.items


# Operator overloading: familiar operators now work with Vector objects.
first = Vector(2, 3)
second = Vector(4, 1)
print("first:", first)                     # __str__
print("developer representation:", repr(first))  # __repr__
print("first + second:", first + second)  # __add__
print("first - second:", first - second)  # __sub__
print("first * 3:", first * 3)            # __mul__
print("3 * first:", 3 * first)            # __rmul__
print("Vectors equal:", first == Vector(2, 3))  # __eq__

# Collection-style dunder methods make ShoppingCart work with Python syntax.
cart = ShoppingCart(["book", "pen", "notebook"])
print("Number of items:", len(cart))
print("First item:", cart[0])
print("Contains pen:", "pen" in cart)
print("All items:")
for item in cart:
    print("-", item)

# Common dunder methods covered here:
# __init__  initialize an object
# __str__ / __repr__  convert an object to readable/debug text
# __add__ / __sub__ / __mul__ / __rmul__  overload arithmetic operators
# __eq__  define equality comparison
# __len__ / __iter__ / __getitem__ / __contains__ support collection operations
