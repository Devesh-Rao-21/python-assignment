#1. Write a program to print your name.  
# a=("My name is Devesh")
# print (a)

#2. Write a program for a Single line comment and multi-line comments 
# For a single line comment use "#" at the beginning of the line.
# And for multi line comment select the lines and press ( ctrl+ / ) , to comment multi lines.

#3. Define variables for different Data Types int, Boolean, char, float, double and print on the 
#Console
# Integer
age = 25

# Boolean
is_student = True

# Character (string of length 1)
grade = 'A'

# Float (covers double precision as well)
gpa = 3.85

print(f"Age: {age}")
print(f"Is student: {is_student}")
print(f"Grade: {grade}")
print(f"GPA: {gpa}")

#4. Define the local and Global variables with the same name and print both variables and 
#understand the scope of the variables
# Global variable
x = 10

def print_variables():
    # Local variable with the same name
    x = 20
    print(f"Local x: {x}")

# Call the function
print_variables()

# Print the global variable
print(f"Global x: {x}")