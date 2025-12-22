# Write a program to print  “Bright IT Career”  ten times using for loop 
for i in range(10):
    print("Bright IT Career")

# Write a java program to print 1 to 20 numbers using the while loop
count = 1
while count <= 20:
    print(count)
    count += 1

#Program to equal operator and not equal operators 
a = 10
b = 5

print(f"Is a equal to b? {a == b}")
print(f"Is a not equal to b? {a != b}")

# Write a program to print the odd and even numbers
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

#Write a program to print largest number among three numbers
num1 = 10
num2 = 20
num3 = 15

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")

#Write a  program to print even number between 10 and 20 using while 
num = 10
while num <= 20:
    if (num % 2) == 0:
        print(num)
    num += 1
#Write a program to print 1 to 10 using the do-while loop statement
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

# Write a program to find Armstrong number or not 
num = 153 # Example number
sum = 0
temp = num
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

#Write a program to find the prime or not
num = 11 # Example number

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

#Write a program to palindrome or not
text = "madam" # Example text

if text == text[::-1]:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")

#Program to check whether a number is EVEN or ODD using switch
def check_even_odd(number):
    # Use dictionary mapping as Python alternative to switch/case
    return {
        0: "Even",
        1: "Odd",
    }.get(number % 2, "Unknown")
num = 7 # Example number
result = check_even_odd(num)
print(f"{num} is {result}")

#Print gender (Male/Female) program according to given M/F using switch
def get_gender(char):
    # Use dictionary mapping as Python alternative to switch/case
    return {
        'M': "Male",
        'F': "Female",
        'm': "Male",
        'f': "Female",
    }.get(char, "Unknown Gender")

gender_char = 'M' # Example input
result = get_gender(gender_char)
print(f"The gender for input '{gender_char}' is: {result}")