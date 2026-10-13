# Understanding super() in Python
#
# MRO means Method Resolution Order.
# It is the order Python follows when looking for a method.
# For Dog, Python checks Dog first, then Animal, and then object.
# super() tells Python: "Continue looking after the current class."
# This lets Dog reuse Animal's code instead of writing it again.


# -----------------------------------------------------
# 1. Basic use: call the parent initializer
# -----------------------------------------------------
class Animal:
    def __init__(self, name):
        print("Animal.__init__ runs")
        self.name = name

    def describe(self):
        return f"I am {self.name}."


class Dog(Animal):
    def __init__(self, name, breed):
        # Python is in Dog, so super() continues the search in Animal.
        # Animal sets the name; Dog sets its own breed.
        super().__init__(name)
        self.breed = breed

    def describe(self):
        # Get Animal's description, then add Dog-specific information.
        animal_description = super().describe()
        return f"{animal_description} I am a {self.breed}."


print("--- Basic super() use ---")
dog = Dog("Buddy", "Labrador")
print(dog.describe())
# This printed list shows the order Python checks for Dog's methods.
print("Dog MRO:", [class_type.__name__ for class_type in Dog.mro()])


# -----------------------------------------------------
# 2. What happens without super()?
# -----------------------------------------------------
# If Dog.__init__ did not call super().__init__(name), Animal.__init__ would
# not run and dog.name would never be created. Calling the base method directly
# (Animal.__init__(self, name)) can work in simple cases, but is less flexible
# when the class hierarchy changes or uses multiple inheritance.


# -----------------------------------------------------
# 3. super() in multiple inheritance (cooperative calls)
# -----------------------------------------------------
# When a class has multiple parents, the MRO decides which class comes next.
# super() continues through that list; it does not always mean "my direct
# parent." Each class uses its own data and passes the remaining data along.
class Person:
    def __init__(self, name, **kwargs):
        print("Person initializer")
        super().__init__(**kwargs)
        self.name = name


class Employee(Person):
    def __init__(self, employee_id, **kwargs):
        print("Employee initializer")
        super().__init__(**kwargs)
        self.employee_id = employee_id


class Student(Person):
    def __init__(self, student_id, **kwargs):
        print("Student initializer")
        super().__init__(**kwargs)
        self.student_id = student_id


class TeachingAssistant(Employee, Student):
    def __init__(self, name, employee_id, student_id):
        print("TeachingAssistant initializer")
        super().__init__(
            name=name,
            employee_id=employee_id,
            student_id=student_id,
        )


print("\n--- Cooperative multiple inheritance ---")
assistant = TeachingAssistant("Asha", "E17", "S42")
print("Name:", assistant.name)
print("Employee ID:", assistant.employee_id)
print("Student ID:", assistant.student_id)
# Python checks these classes in this order when looking for a method.
print(
    "TeachingAssistant MRO:",
    [class_type.__name__ for class_type in TeachingAssistant.mro()],
)


# -----------------------------------------------------
# Key points
# -----------------------------------------------------
# - MRO is Python's method-search order: the class, its parent classes, then
#   object.
# - super() continues that search after the class whose method is running.
# - In multiple inheritance, classes should call super() and pass along data
#   they do not use. This lets every class in the MRO participate.
# - Use ClassName.mro() to see the search order.
