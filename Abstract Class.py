# 1. Create an abstract class with abstract and non-abstract methods. 
from abc import ABC, abstractmethod

class Animal(ABC): # Inherit from ABC to make it an abstract class
    @abstractmethod
    def make_sound(self): # Abstract method (no implementation)
        pass

    def move(self): # Non-abstract (concrete) method
        print("The animal is moving.")

# 2. Create a sub class for an abstract class. Create an object in the child class for the  
# abstract class and access the non-abstract methods 
class Dog(Animal): # Dog is a subclass of Animal
    def make_sound(self):
        # We must implement the abstract method from the parent class
        print("Woof! Woof!")

# Attempting to create an object of the abstract class (Animal) will fail:
# animal_obj = Animal() 
# This line raises: TypeError: Can't instantiate abstract class Animal with abstract method make_sound

# 3. Create an instance for the child class in child class and call abstract methods 
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        print("The animal is moving.")

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

# Create an instance of the concrete subclass (Dog)
dog_instance = Dog()

# Call the 'make_sound' method, which was abstract in the parent class
print("Calling the implemented abstract method 'make_sound':")
dog_instance.make_sound() # Output: Woof! Woof!

# 4. Create an instance for the child class in child class and call non-abstract methods
# Create an instance of the concrete subclass (Dog)
dog_instance = Dog()

# Call the implemented abstract method (from problem #3)
print("Calling abstract method:")
dog_instance.make_sound() # Output: Woof! Woof!

# Call the inherited non-abstract method (from problem #4)
print("\nCalling non-abstract method:")
dog_instance.move() # Output: The animal is moving.