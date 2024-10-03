# # Function to square a number
# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]
# # Apply the square function to all numbers
# squared_numbers = list(map(square, numbers))

# print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Function to check if a number is even
# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6]
# # Filter out the odd numbers
# even_numbers = list(filter(is_even, numbers))

# print(even_numbers)  # Output: [2, 4, 6]


from functools import reduce

# Function to multiply two numbers
def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
# Multiply all numbers together
result = reduce(multiply, numbers)

print(result)  # Output: 24


result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 24