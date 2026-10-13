# Encapsulation Example in Python
# Encapsulation binds data and methods inside a class.
# It also restricts direct access to some parts of an object.
# This helps protect important data and control how values are changed.

# Define a class named Student.
class Student:
    # Constructor to initialize name and age.
    def __init__(self, name, age):
        self.name = name            # public attribute: accessible from outside
        self.age = age  # The property setter validates and stores the age.

    # Traditional getter method to access the private attribute __age.
    def get_age(self):
        return self.__age

    # Traditional setter method with validation before updating the data.
    def set_age(self, age):
        if age > 0:
            self.__age = age        # valid age, update the value
        else:
            print("Invalid age!")  # invalid value, do not update

    # @property turns a method into an attribute-style getter.
    @property
    def age(self):
        return self.__age

    # @age.setter defines the matching attribute-style setter.
    # The property keeps validation in one place while callers use student.age.
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError("Age must be greater than zero.")


# Create an object of Student.

student1 = Student("Alice", 20)

# Access public attribute directly.
print("Name:", student1.name)

# Access private attribute through a getter method.
print("Age (using getter):", student1.get_age())

# Update age using setter method.
student1.set_age(21)
print("Updated Age:", student1.get_age())

# A property provides getter/setter behavior with natural attribute syntax.
print("Age (using @property):", student1.age)
student1.age = 22
print("Updated age (using @property):", student1.age)

# The following assignment raises ValueError because the property validates it.
# student1.age = -1

# This line would raise an AttributeError because __age is private.
# print(student1.__age)

# Encapsulation is useful because it protects data integrity.
# For example, we can prevent invalid values like negative age or zero age.
