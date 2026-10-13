# Class and Object in Python
# OOP stands for Object-Oriented Programming.
# A class is a blueprint or template for creating objects.
# An object is an actual instance of a class.
# Example: class Person -> objects like person1, person2
from datetime import date


# -----------------------------------------------------
# 1. Creating a class
# -----------------------------------------------------
class Person:
    # Class variable
    # This is shared by all objects created from this class.
    # It belongs to the class, not to one particular object.
    country = "India"
    people_count = 0

    # Constructor
    # __init__() is called automatically when an object is created.
    # It is used to initialize instance variables.
    def __init__(self, name, age):
        # Instance variables
        # These values are unique for each object.
        self.name = name
        self.age = age
        Person.people_count += 1

    # Instance method
    # This method works on an object and can access instance variables.
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")

    # Another method showing how methods can use object data.
    def greet(self):
        print(f"Hello, my name is {self.name}.")

    # Example of a method updating an object value.
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! {self.name} is now {self.age} years old.")

    # Class method: receives the class as its first argument (cls).
    # Use it for behavior involving class-level data or alternate constructors.
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    @classmethod
    def get_people_count(cls):
        return cls.people_count

    # Static method: receives neither self nor cls automatically.
    # It is grouped in the class because the helper is related to Person.
    @staticmethod
    def is_valid_age(age):
        return age >= 0


# -----------------------------------------------------
# 2. Creating objects
# -----------------------------------------------------
# person1 and person2 are objects (instances) of the class Person.
person1 = Person("Rupesh", 35)
person2 = Person("Vidya", 30)

# Accessing instance variables using object.
print("person1.name:", person1.name)
print("person1.age:", person1.age)
print("person2.name:", person2.name)
print("person2.age:", person2.age)

# Accessing class variable using object.
print("person1.country:", person1.country)
print("person2.country:", person2.country)

# -----------------------------------------------------
# 3. Calling methods
# -----------------------------------------------------
person1.display_info()
person2.greet()

# -----------------------------------------------------
# 4. How self is used
# -----------------------------------------------------
# self refers to the current object instance.
# It is the first parameter in instance methods.
# self.name and self.age refer to the current object's attributes.
# Python passes the object as the first argument to instance methods.

# Example: person1.display_info() means Python internally does something like:
# Person.display_info(person1)

# -----------------------------------------------------
# 5. Difference between class variable and instance variable
# -----------------------------------------------------
# Class variable: same for all objects of the class.
# Instance variable: different for each object.
# Here, country is a class variable because all Person objects share it.
# name and age are instance variables because each object has its own values.

# -----------------------------------------------------
# 6. Instance methods, class methods, and static methods
# -----------------------------------------------------
# Instance methods receive self and work with one object's data.
# Class methods receive cls and work with class-level data or create instances.
# Static methods receive no automatic first argument.
# They act as helpers grouped with the class.
person3 = Person.from_birth_year("Sam", 2000)
# This class method acts as an alternate constructor.
print("Person created from birth year:", person3.name, person3.age)
print("Valid age 25:", Person.is_valid_age(25))  # static method
print("Valid age -2:", Person.is_valid_age(-2))
print("Number of people:", Person.get_people_count())

# -----------------------------------------------------
# 7. Using constructor and methods together
# -----------------------------------------------------
person1.celebrate_birthday()
person1.display_info()

# -----------------------------------------------------
# 8. Summary
# -----------------------------------------------------
# - Class = blueprint
# - Object = actual instance created from the class
# - Instance variables = unique to each object
# - Class variables = shared by all objects
# - Methods = functions inside a class
# - __init__() = constructor used to initialize object data
# - self = current object instance
