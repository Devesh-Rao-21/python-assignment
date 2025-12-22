#1. Different ways creating a string 
# Single quotes
str1 = 'Hello'

# Double quotes
str2 = "World"

# Multiline string using triple quotes
str3 = """This is a 
multiline string."""

# 2. Concatenating two strings using + operator 
greeting = str1 + " " + str2 # Output: "Hello World"

# 3. Finding the length of the string 
length = len(greeting) # Output: 11

# 4. Extract a string using Substring 
substring = greeting[0:5] # Extracts characters from index 0 up to (but not including) 5. Output: "Hello"
substring2 = greeting[6:] # Extracts from index 6 to the end. Output: "World"

# 5. Searching in strings using index() 
pos = greeting.index("World") # Output: 6
# pos_error = greeting.index("Mars") # This would raise a ValueError

# 6. Matching a String Against a Regular Expression With matches()
import re

text = "The rain in Spain"
# Check if the string starts with "The"
match = re.search("^The", text) 
if match:
    print("Match found at the beginning.")

# 7. Comparing strings  
s1 = "Python"
s2 = "python"
are_equal_value = (s1 == s2) # Output: False (case-sensitive)
are_equal_identity = (s1 is s2) # Checks if they are the exact same object in memory

# 8. startsWith(), endsWith() and compareTo() 
text = "Python programming"
starts = text.startswith("Python") # Output: True
ends = text.endswith("ming")      # Output: True

# 9. Trimming strings with strip() 
spaced_text = "  Hello World  "
trimmed_text = spaced_text.strip() # Output: "Hello World"

# 10. Replacing characters in strings with replace() 
original = "apple pie, apple sauce"
new_string = original.replace("apple", "orange") # Output: "orange pie, orange sauce"
partial_replace = original.replace("apple", "orange", 1) # Replaces only the first instance

# 11. Splitting strings with split() 
data = "apple,banana,cherry"
fruits_list = data.split(",") # Output: ['apple', 'banana', 'cherry']

sentence = "This is a sentence"
words_list = sentence.split() # Splits by whitespace. Output: ['This', 'is', 'a', 'sentence']

# 12. Converting integer objects to Strings 
number = 123
string_number = str(number) # Output: "123" (as a string)

f_string_conversion = f"The number is {number}" # Automatic conversion within f-string

# 13. Converting to uppercase and lowercase
case_text = "HeLLo WoRLD"
upper_text = case_text.upper() # Output: "HELLO WORLD"
lower_text = case_text.lower() # Output: "hello world"