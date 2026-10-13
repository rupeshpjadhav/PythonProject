# Abstraction Example in Python
# Abstraction means hiding complex implementation details and showing only the necessary features.
# In OOP, abstraction helps us focus on what an object does rather than how it does it.
# Python supports abstraction using the abc module.

# Importing ABC (Abstract Base Class) and abstractmethod from abc module.
# ABC is used to create abstract classes, and abstractmethod marks methods that must be implemented.
from abc import ABC, abstractmethod

# Defining an abstract class named Vehicle.
# An abstract class is a blueprint for other classes and cannot be instantiated directly.
class Vehicle(ABC):
    # Abstract method: must be implemented by subclasses.
    # This ensures that every vehicle type provides the required behavior.
    @abstractmethod
    def start(self):
        pass  # No implementation here; it is just a placeholder.

    # Another abstract method.
    @abstractmethod
    def stop(self):
        pass  # No implementation here; subclass must define this behavior.

# Concrete class Car inherits from Vehicle.
# A concrete class is a normal class that can be instantiated.
class Car(Vehicle):
    # This method implements the abstract start() method from Vehicle.
    def start(self):
        print("Car started.")

    # This method implements the abstract stop() method from Vehicle.
    def stop(self):
        print("Car stopped.")

# Creating an object of Car.
# This works because Car implements all abstract methods from Vehicle.
car = Car()

# Calling the methods defined in the subclass.
car.start()
car.stop()

# In real life, abstraction helps us work with a generic concept like "Vehicle"
# without worrying about the internal details of each specific vehicle type like Car, Bike, or Truck.
