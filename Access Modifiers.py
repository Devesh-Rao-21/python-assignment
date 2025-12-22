# 1. Create a class with PRIVATE fields, private method and a main method. Print the fields 
# in main method. Call the private method in main method. 
# Create a sub class and try to access the private fields and methods from sub class.
class PrivateExample:
    def __init__(self):
        self.__private_field = "This is a private field." # Private attribute
    
    def __private_method(self): # Private method
        print("This is a private method.")

    def public_access_method(self): # Public method to access private members internally
        print(self.__private_field) # Works inside the class
        self.__private_method() # Works inside the class

# Main execution area
obj = PrivateExample()
obj.public_access_method() 

# Trying to access directly from outside the class results in an AttributeError
try:
    print(obj.__private_field)
except AttributeError as e:
    print(f"Error: {e}") 

# You can technically access it using the mangled name, but this is highly discouraged
print(obj._PrivateExample__private_field) # Works, but breaks encapsulation convention

# 2. Create a class with PROTECTED fields and methods. Access these fields and methods 
# from any other class in the same package.  
# Also, Access the PROTECTED fields and methods from child class located in a different 
# package 
# Access the PROTECTED fields and methods from any class in different package 
class ProtectedExample:
    def __init__(self):
        self._protected_field = "This is a protected field." # Protected attribute

    def _protected_method(self): # Protected method
        print("This is a protected method.")

class SubClass(ProtectedExample):
    def access_protected(self):
        # Accessing protected members in a subclass works as intended
        print(f"Accessing from subclass: {self._protected_field}")
        self._protected_method()

# Main execution area
sub_obj = SubClass()
sub_obj.access_protected()

# They can also be accessed directly outside the class, although this is discouraged
print(f"Accessing directly outside: {sub_obj._protected_field}")

# 3. Create a class with PUBLIC fields and methods.  
# Access the public methods and fields from any class in the same package or different 
# package.
class PublicExample:
    def __init__(self, name):
        self.public_field = name # Public attribute

    def public_method(self): # Public method
        print(f"This is a public method. Field value: {self.public_field}")

# Main execution area
obj = PublicExample("Public Data")

# Accessing public members from anywhere works
print(obj.public_field)
obj.public_method()
