#A, B and C are classes 
# A is a super class. B is a sub class of A. C is a sub class of B.  
# Create three methods in each class, 2 methods are specific to each class and third 
# method (override method) should be in all three Classes A, B and C 
# Create a class with main method. Create an object for each class A, B and C in main 
# method and call every method of each class using its own object/instance. 
# Call an overridden method with super class reference to B and C class’s objects 
# Runtime Polymorphism with Data Members/Instance variables, Repeat the above 
# process only for data members
# Class A (Super class)
class A:
    data_member = "Data in Class A"  # Class/Instance variable

    def method_a1(self):
        print("Class A - Specific Method 1")

    def method_a2(self):
        print("Class A - Specific Method 2")

    # Overridden method
    def override_method(self):
        print("Class A - Overridden Method Implementation")

# Class B (Sub class of A)
class B(A):
    data_member = "Data in Class B"  # Hides the data member in A

    def method_b1(self):
        print("Class B - Specific Method 1")

    def method_b2(self):
        print("Class B - Specific Method 2")

    # Overriding the method from A
    def override_method(self):
        print("Class B - Overridden Method Implementation")

# Class C (Sub class of B)
class C(B):
    data_member = "Data in Class C"  # Hides the data member in B and A

    def method_c1(self):
        print("Class C - Specific Method 1")

    def method_c2(self):
        print("Class C - Specific Method 2")

    # Overriding the method from B
    def override_method(self):
        print("Class C - Overridden Method Implementation")

# Main execution block
if __name__ == "__main__":
    # Create objects for each class A, B and C and call every method of each class
    print("--- Calling methods with their own class objects ---")
    obj_a = A()
    obj_a.method_a1()
    obj_a.method_a2()
    obj_a.override_method()
    print(f"Data Member: {obj_a.data_member}")
    print()

    obj_b = B()
    obj_b.method_b1()
    obj_b.method_b2()
    obj_b.override_method()
    # obj_b.method_a1() # Can also call inherited methods from A
    print(f"Data Member: {obj_b.data_member}")
    print()

    obj_c = C()
    obj_c.method_c1()
    obj_c.method_c2()
    obj_c.override_method()
    # obj_c.method_a1() # Can also call inherited methods from A/B
    print(f"Data Member: {obj_c.data_member}")
    print()

    # Call an overridden method with super class reference (variable) to B and C class's objects

    print("--- Demonstrating Runtime Polymorphism (Methods) ---")
    # In Python, variable types are dynamic. The reference effectively takes the type of the assigned object.
    ref_to_b = B()
    # The method called is determined dynamically based on the actual object instance (B).
    ref_to_b.override_method()  # Calls B's implementation

    ref_to_c = C()
    # The method called is determined dynamically based on the actual object instance (C).
    ref_to_c.override_method()  # Calls C's implementation
    print()

    # Runtime Polymorphism with Data Members/Instance variables
    print("--- Demonstrating Attribute Access/Hiding (Not Polymorphism) ---")
    # Python accesses the attribute based on the object's instance dictionary and inheritance chain traversal.

    # When accessing data_member on these objects, Python finds the attribute in the actual B or C class scope first.
    print(f"Variable assigned B object, accessing data_member: {ref_to_b.data_member}") # Accesses B's data_member
    print(f"Variable assigned C object, accessing data_member: {ref_to_c.data_member}") # Accesses C's data_member