# 1. Write two methods with the same name but different number of parameters of same type 
# and call the methods  
class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            print(f"Sum of three numbers: {a + b + c}")
        else:
            print(f"Sum of two numbers: {a + b}")

# Create an object and call the method
obj = Calculator()
obj.add(10, 20)
obj.add(10, 20, 30)

# 2. Write two methods with the same name but different number of parameters of different 
# data type and call the methods  
class Messenger:
    def send_message(self, recipient, message=None):
        if message is None:
            print(f"Sending a default message to {recipient}")
        else:
            print(f"Sending '{message}' to {recipient}")

# Using a single method with conditional logic
m = Messenger()
m.send_message("Alice")
m.send_message("Bob", 42) # Python handles the different types dynamically

# 3. Write two methods with the same name and same number of parameters of same type  
class Processor:
    # A single method handles different logic internally based on 'mode'
    def process_data(self, data: int, count: int, mode: str):
        if mode == "simple":
            result = data * count
            print(f"Simple processing result: {result}")
        elif mode == "complex":
            result = data ** count
            print(f"Complex processing result: {result}")
        else:
            print("Unknown mode provided.")

# Create an object and call the method with different modes
p = Processor()
p.process_data(5, 2, "simple")  # Performs 5 * 2
p.process_data(5, 2, "complex") # Performs 5 ** 2