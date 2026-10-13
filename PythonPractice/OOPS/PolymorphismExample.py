# Polymorphism Example in Python
# Polymorphism means "many forms".
# In OOP, it allows the same method name to behave differently depending on the object calling it.
# This makes code more flexible and reusable.

# Base class named Shape.
# It defines a common method signature that subclasses must implement.
class Shape:
    def area(self):
        pass  # To be implemented by each subclass

# Derived class 1: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Rectangle implements area() differently from Circle.
    def area(self):
        return self.width * self.height

# Derived class 2: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Circle calculates its area using the circle formula.
    def area(self):
        return 3.14 * self.radius * self.radius

# Using polymorphism.
# The same method name area() is called on different objects,
# but each object executes the version appropriate for its class.
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}")

# This works because both Rectangle and Circle implement the area() method.
# Polymorphism allows us to treat them as objects of the same base type while using their specific behavior.
