# 1. Write a program to generate Arithmetic Exception without exception handling 
# Program 1: Generate Arithmetic Exception without handling
numerator = 10
denominator = 0
result = numerator / denominator  # This line will raise a ZeroDivisionError
print(f"Result: {result}")

# 2. Handle the Arithmetic exception using try-catch block 
# Program 2: Handle Arithmetic exception using try-except
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
print("Program continues after the exception handling.")

# 3. Write a method which throws exception, Call that method in main class without try block 
# Program 3: Method that raises exception, called without try block
def risky_method(a, b):
    if b == 0:
        # We can explicitly raise an exception
        raise ZeroDivisionError("Cannot divide by zero in risky_method")
    return a / b

# Calling the method without a try block will cause the program to crash
result = risky_method(10, 0)
print(f"Result: {result}")

# 4. Write a program with multiple catch blocks 
# Program 4: Multiple except blocks
try:
    user_input = input("Enter a number: ")
    num = int(user_input)
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 5. Write a program to throw exception with your own message 
# Program 5: Raise exception with a custom message
age = -5
if age < 0:
    raise ValueError(f"Age cannot be negative; received: {age}")

# 6. Write a program to create your own exception 
# Program 6: Create a custom exception
class InvalidSpeedError(Exception):
    """Exception raised for invalid speed values."""
    def __init__(self, speed, message="Speed is out of allowed range (0-100)"):
        self.speed = speed
        self.message = message
        super().__init__(self.message)

try:
    speed = 120
    if speed > 100 or speed < 0:
        raise InvalidSpeedError(speed)
except InvalidSpeedError as e:
    print(f"Handled error: {e.message} (Speed: {e.speed})")

# 7. Write a program with finally block 
# Program 7: Program with a finally block
try:
    f = open("non_existent_file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    print("The finally block always executes, even with an error.")

# 8. Write a program to generate Arithmetic Exception 
# Program 8: Generate Arithmetic Exception
# This will cause a ZeroDivisionError
print(10 / 0)

# 9. Write a program to generate FileNotFoundException 
# Program 9: Generate FileNotFoundError
# Make sure "imaginary_file.txt" does not exist in the current directory
with open("imaginary_file.txt", "r") as file:
    content = file.read()

# 10. Write a program to generate ClassNotFoundException 
# Program 10: Python equivalent to ClassNotFoundException
# Attempting to import a module that likely does not exist
# import non_existent_module

# 11. Write a program to generate IOException 
# Program 11: Generate an I/O Error (e.g., permission denied)
# This might fail if you don't have write permissions to the root directory
try:
    with open("/root/unwritable_file.txt", "w") as f:
        f.write("Hello")
except IOError as e:
    print(f"Caught an I/O Error: {e}")

# 12. Write a program to generate NoSuchFieldException
# Program 12: Python equivalent to NoSuchFieldException
class MyClass:
    def __init__(self):
        self.existing_field = "value"

obj = MyClass()
# This will raise an AttributeError because 'non_existent_field' does not exist
print(obj.non_existent_field)
