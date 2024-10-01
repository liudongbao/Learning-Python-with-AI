# def greet():
#     print("Hello, welcome to Python functions!")

# greet()  # This will call the function


# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice Aunt")  # Passes the argument "Alice" to the function

# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 30)
# print("The sum is:", result)

# def greet(name="Guest"):
#     print(f"Hello, {name}!")

# greet()         # Uses default value "Guest"
# greet("John")   # Uses provided argument "John"

# def divide(a, b):
#     quotient = a // b
#     remainder = a % b
#     return quotient, remainder

# q, r = divide(10, 4)
# print("Quotient:", q)
# print("Remainder:", r)

def is_even(number):
    return number % 2 == 0

for i in range(1, 3):
    if is_even(i):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")