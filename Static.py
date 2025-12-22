#1. Define a static variable and access that through a class 
class MyClass:
    # Define a class variable (static variable)
    class_var = "Static Variable Value"

# Access the static variable through the class name
print(MyClass.class_var)

#2. Define a static variable and access that through a instance
class MyClass:
    class_var = "Static Value"

# Create an instance
obj = MyClass()

# Access the static variable through the instance
print(obj.class_var)

#3. Define a static variable and change within the instance
class MyClass:
    class_var = "Original Value"

obj1 = MyClass()
obj2 = MyClass()

# Access the original class variable
print(f"Original: {MyClass.class_var}") # Output: Original Value
print(f"Obj1 before change: {obj1.class_var}") # Output: Original Value

# Change the value through the instance (creates a new instance variable for obj1)
obj1.class_var = "New Instance Value"

# Verify the change for obj1 and the original for obj2 and the class
print(f"Obj1 after change: {obj1.class_var}") # Output: New Instance Value
print(f"Obj2: {obj2.class_var}") # Output: Original Value (unaffected)
print(f"Class: {MyClass.class_var}") # Output: Original Value (unaffected)

#4. Define a static variable and change within the class
class MyClass:
    class_var = "Value A"

obj1 = MyClass()
obj2 = MyClass()

# Verify initial value
print(f"Obj1 before change: {obj1.class_var}") # Output: Value A
print(f"Obj2 before change: {obj2.class_var}") # Output: Value A

# Change the value through the class name
MyClass.class_var = "Value B"

# Verify that all instances see the updated value
print(f"Obj1 after class change: {obj1.class_var}") # Output: Value B
print(f"Obj2 after class change: {obj2.class_var}") # Output: Value B
