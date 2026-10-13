# OOP Concepts Comparison in Python
# This file explains the most important OOP concepts in a simple way.
# These are: Inheritance, Polymorphism, Encapsulation, and Abstraction.

# -----------------------------------------------------
# 1. INHERITANCE
# -----------------------------------------------------
# Inheritance means a child class can reuse the features of a parent class.
# This reduces duplication and promotes code reuse.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

print("--- Inheritance ---")
dog = Dog("Buddy")
cat = Cat("Milo")
dog.speak()
cat.speak()

# -----------------------------------------------------
# 2. POLYMORPHISM
# -----------------------------------------------------
# Polymorphism means the same method name can behave differently depending on the object.
# The same method name works in different ways in different classes.

class Bird:
    def sound(self):
        print("Bird makes a sound")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

class Parrot(Bird):
    def sound(self):
        print("Parrot repeats words")

print("\n--- Polymorphism ---")
for animal in [Sparrow(), Parrot()]:
    animal.sound()

# -----------------------------------------------------
# 3. ENCAPSULATION
# -----------------------------------------------------
# Encapsulation means wrapping data and methods together inside a class.
# It also restricts direct access to some data using private variables.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

print("\n--- Encapsulation ---")
account = BankAccount(1000)
print("Initial balance:", account.get_balance())
account.deposit(500)
print("Updated balance:", account.get_balance())

# Note:
# account.__balance cannot be accessed directly from outside the class.
# This protects the internal state of the object.

# -----------------------------------------------------
# 4. ABSTRACTION
# -----------------------------------------------------
# Abstraction hides the internal implementation details and shows only the necessary features.
# It focuses on what an object does, not how it does it.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

print("\n--- Abstraction ---")
car = Car()
bike = Bike()
car.start()
bike.start()

# -----------------------------------------------------
# 5. SIMPLE COMPARISON
# -----------------------------------------------------
# Inheritance: one class gets properties from another.
# Polymorphism: same name, different behavior.
# Encapsulation: protect data and control access.
# Abstraction: hide complex implementation and show only required behavior.

# -----------------------------------------------------
# 6. SUMMARY
# -----------------------------------------------------
# These four concepts are the foundation of OOP in Python.
# They help us write cleaner, reusable, and organized code.
