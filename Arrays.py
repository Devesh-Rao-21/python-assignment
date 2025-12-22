#1. Write a function to add integer values of an array 
def add_array_integers(arr):
    """
    Calculates the sum of all integer values in a list (array).
    """
    # Use the built-in sum function to add all elements
    total = sum(arr)
    return total

# Example usage:
my_array = [10, 20, 30, 40]
# Answer: **100**
print(f"The sum of the array is: {add_array_integers(my_array)}")

#2. Write a function to calculate the average value of an array of integers 
def calculate_average(arr):
    """
    Calculates the average value of an array of integers.
    Returns 0 if the array is empty to avoid division by zero error.
    """
    if not arr:
        return 0
    # Calculate sum and length, then divide to find the average
    total = sum(arr)
    count = len(arr)
    average = total / count
    return average

# Example usage:
my_array = [10, 20, 30, 40]
# Answer: **25.0**
print(f"The average of the array is: {calculate_average(my_array)}")

#3. Write a program to find the index of an array element
def find_element_index(arr, element_to_find):
    """
    Finds the index of a specific element in the array.
    Uses try-except to handle cases where the element is not found.
    """
    try:
        # Use the index() method to find the position of the element
        index = arr.index(element_to_find)
        return index
    except ValueError:
        return -1 # Return -1 or handle the error as appropriate

# Example usage:
my_array = [10, 2, 30, 4, 5]
element = 30
# Answer: **2**
print(f"The index of {element} is: {find_element_index(my_array, element)}")

element = 100
# Answer: **-1**
print(f"The index of {element} is: {find_element_index(my_array, element)}")

#4. Write a function to test if array contains a specific value 
def contains_value(arr, value):
    """
    Tests if an array contains a specific value using the 'in' operator.
    """
    # The 'in' operator returns True if the value is found, False otherwise
    return value in arr

# Example usage:
my_array = [1, 2, 3, 4, 5]
value_to_check = 3
# Answer: **True**
print(f"Does the array contain {value_to_check}? {contains_value(my_array, value_to_check)}")

value_to_check = 10
# Answer: **False**
print(f"Does the array contain {value_to_check}? {contains_value(my_array, value_to_check)}")

#5. Write a function to remove a specific element from an array
def remove_element(arr, element_to_remove):
    """
    Removes a specific element from an array in place.
    """
    try:
        # The remove() method modifies the list directly (in place)
        arr.remove(element_to_remove)
        return True, arr
    except ValueError:
        return False, arr # Element not found

# Example usage:
my_array = [10, 20, 30, 40, 30]
element = 30
success, updated_array = remove_element(my_array, element)
# Answer: **[10, 20, 40, 30]** (after removing the first 30)
print(f"Removed {element}? {success}. Updated array: {updated_array}")

#6. Write a function to copy an array to another array
def copy_array(original_arr):
    """
    Copies an array to a new array using the copy() method.
    """
    # Creates a new list instance with the same elements
    new_array = original_arr.copy()
    return new_array

# Example usage:
original = [1, 2, 3]
copied = copy_array(original)
# Answer: **[1, 2, 3]**
print(f"Original: {original}, Copied: {copied}")

# Verify they are independent:
copied.append(4)
print(f"Original after modification: {original}, Copied after modification: {copied}")

#7. Write a function to insert an element at a specific position in the array
def insert_element(arr, position, element):
    """
    Inserts an element at a specific position (index) in the array.
    """
    # Inserts the element before the specified index
    arr.insert(position, element)
    return arr

# Example usage:
my_array = [10, 20, 40, 50]
position_index = 2
element_to_insert = 30
updated_array = insert_element(my_array, position_index, element_to_insert)
# Answer: **[10, 20, 30, 40, 50]**
print(f"Array after insertion: {updated_array}")

#8. Write a function to find the minimum and maximum value of an array 
def find_min_max(arr):
    """
    Finds the minimum and maximum values of an array using built-in functions.
    """
    if not arr:
        return None, None
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum

# Example usage:
my_array = [5, 2, 9, 1, 5, 6]
minimum_val, maximum_val = find_min_max(my_array)
# Answer: **Min: 1, Max: 9**
print(f"Minimum value: {minimum_val}, Maximum value: {maximum_val}")

#9. Write a function to reverse an array of integer values
def reverse_array_inplace(arr):
    """
    Reverses the elements of an array in place.
    """
    arr.reverse()
    return arr

def reverse_array_new(arr):
    """
    Returns a new reversed array using slicing.
    """
    return arr[::-1]

# Example usage (in-place):
my_array = [1, 2, 3, 4, 5]
reversed_array = reverse_array_inplace(my_array)
# Answer: **[5, 4, 3, 2, 1]**
print(f"In-place reversed array: {reversed_array}")

#10. Write a function to find the duplicate values of an array 
from collections import Counter

def find_duplicates(arr):
    """
    Finds and returns a list of duplicate values in an array.
    """
    # Count occurrences of each element
    counts = Counter(arr)
    # Filter for elements where the count is greater than 1
    duplicates = [item for item, count in counts.items() if count > 1]
    return duplicates

# Example usage:
my_array = [1, 2, 3, 2, 4, 1, 5, 3]
duplicate_values = find_duplicates(my_array)
# Answer: **[1, 2, 3]**
print(f"Duplicate values: {duplicate_values}")

#11. Write a program to find the common values between two arrays
def find_common_values(arr1, arr2):
    """
    Finds common values between two arrays using set intersection.
    """
    # Convert lists to sets to find intersection efficiently
    set1 = set(arr1)
    set2 = set(arr2)
    # The intersection returns common elements
    common = list(set1 & set2)
    return common

# Example usage:
array_a = [1, 2, 3, 4, 5]
array_b = [4, 5, 6, 7, 8]
common_values = find_common_values(array_a, array_b)
# Answer: **[4, 5]** (order may vary)
print(f"Common values: {common_values}")

#12. Write a method to remove duplicate elements from an array
def remove_duplicates(arr):
    """
    Removes duplicate elements from an array by converting to a set and back to a list.
    """
    # Sets inherently only store unique values
    unique_elements = list(set(arr))
    return unique_elements

# Example usage:
my_array = [1, 2, 2, 3, 4, 4, 5, 1]
unique_array = remove_duplicates(my_array)
# Answer: **[1, 2, 3, 4, 5]** (order may vary)
print(f"Array with duplicates removed: {unique_array}")

#13. Write a method to find the second largest number in an array 
def find_second_largest(arr):
    """
    Finds the second largest number in an array.
    """
    # Use a set to get unique elements and sort them
    unique_sorted = sorted(list(set(arr)))
    # If there are at least two unique elements, return the second to last
    if len(unique_sorted) >= 2:
        return unique_sorted[-2]
    else:
        return None # Or handle as appropriate if no second largest exists

# Example usage:
my_array = [10, 20, 4, 45, 99, 99]
second_largest = find_second_largest(my_array)
# Answer: **45**
print(f"The second largest number is: {second_largest}")

#15. Write a method to find number of even number and odd numbers in an array 
def count_even_odd(arr):
    """
    Counts the number of even and odd numbers in an array.
    """
    # Filter using list comprehension and modulo operator (%)
    even_numbers = [x for x in arr if x % 2 == 0]
    odd_numbers = [x for x in arr if x % 2 != 0]
    
    count_even = len(even_numbers)
    count_odd = len(odd_numbers)
    
    return count_even, count_odd

# Example usage:
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count, odd_count = count_even_odd(my_array)
# Answer: **Even: 4, Odd: 5**
print(f"Number of even numbers: {even_count}, Number of odd numbers: {odd_count}")

#16. Write a function to get the difference of largest and smallest value 
def difference_min_max(arr):
    """
    Calculates the difference between the largest and smallest value in an array.
    """
    if not arr:
        return 0
    # Difference = Maximum - Minimum
    difference = max(arr) - min(arr)
    return difference

# Example usage:
my_array = [10, 2, 55, 1, 99]
difference = difference_min_max(my_array)
# Answer: **98**
print(f"The difference between largest and smallest is: {difference}")

#17. Write a method to verify if the array contains two specified elements(12,23)
def contains_two_elements(arr, el1, el2):
    """
    Verifies if the array contains two specified elements.
    """
    # Check if both elements are present using 'and' operator
    return el1 in arr and el2 in arr

# Example usage:
my_array = [10, 12, 20, 23, 30]
element1 = 12
element2 = 23
# Answer: **True**
print(f"Does array contain {element1} and {element2}? {contains_two_elements(my_array, element1, element2)}")

element3 = 99
# Answer: **False**
print(f"Does array contain {element1} and {element3}? {contains_two_elements(my_array, element1, element3)}")

#18. Write a program to remove the duplicate elements and return the new array
def return_array_without_duplicates(arr):
    """
    Returns a new array containing only unique elements.
    """
    # Convert to set and back to list
    new_array = list(set(arr))
    return new_array

# Example usage:
original_array = [1, 2, 2, 3, 3, 3, 4]
unique_result = return_array_without_duplicates(original_array)
# Answer: **[1, 2, 3, 4]** (order may vary)
print(f"Original: {original_array}, New unique array: {unique_result}")
