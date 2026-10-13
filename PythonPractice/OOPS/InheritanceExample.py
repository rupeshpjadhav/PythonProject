# Inheritance Types in Python
# Inheritance lets a child class reuse and extend a parent class.


# -----------------------------------------------------
# 1. Single inheritance: one child inherits from one parent.
# -----------------------------------------------------
class Vehicle:
    def move(self):
        print("The vehicle is moving.")


class Car(Vehicle):
    def drive(self):
        print("The car is driving.")


print("--- Single inheritance ---")
car = Car()
car.move()  # inherited from Vehicle
car.drive()  # defined by Car


# -----------------------------------------------------
# 2. Multiple inheritance: one child inherits from multiple parents.
# -----------------------------------------------------
class Flyer:
    def fly(self):
        print("Flying through the air.")


class Swimmer:
    def swim(self):
        print("Swimming through the water.")


class Duck(Flyer, Swimmer):
    pass


print("\n--- Multiple inheritance ---")
duck = Duck()
duck.fly()
duck.swim()


# -----------------------------------------------------
# 3. Multilevel inheritance: a child inherits from a derived class.
# -----------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Mammal(Animal):
    def feed_milk(self):
        print(f"{self.name} feeds its young with milk.")


class Dog(Mammal):
    def speak(self):
        print(f"{self.name} barks.")


print("\n--- Multilevel inheritance ---")
dog = Dog("Buddy")
dog.speak()  # Dog's override
dog.feed_milk()  # inherited from Mammal


# -----------------------------------------------------
# 4. Hierarchical inheritance: multiple children share one parent.
# -----------------------------------------------------
class Shape:
    def describe(self):
        print("I am a shape.")


class Rectangle(Shape):
    def area(self, width, height):
        return width * height


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


print("\n--- Hierarchical inheritance ---")
rectangle = Rectangle()
circle = Circle()
rectangle.describe()
circle.describe()
print("Rectangle area:", rectangle.area(4, 5))
print("Circle area:", circle.area(3))


# -----------------------------------------------------
# 5. Hybrid inheritance: a combination of inheritance patterns.
# -----------------------------------------------------
# TeachingAssistant combines multilevel and multiple inheritance.
# Employee and Student both derive from Person, forming a diamond shape.
class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name


class Employee(Person):
    def __init__(self, employee_id, **kwargs):
        super().__init__(**kwargs)
        self.employee_id = employee_id


class Student(Person):
    def __init__(self, student_id, **kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id


class TeachingAssistant(Employee, Student):
    def __init__(self, name, employee_id, student_id):
        # Cooperative super() follows Python's method resolution order (MRO).
        super().__init__(
            name=name,
            employee_id=employee_id,
            student_id=student_id,
        )

    def describe(self):
        print(
            f"{self.name}: employee #{self.employee_id}, "
            f"student #{self.student_id}"
        )


print("\n--- Hybrid inheritance ---")
assistant = TeachingAssistant("Asha", "E17", "S42")
assistant.describe()
print("MRO:", [class_type.__name__ for class_type in TeachingAssistant.mro()])

# The MRO (method resolution order) determines where Python looks for methods.
# super() follows this order and helps avoid calling a shared parent twice in
# cooperative multiple inheritance.
