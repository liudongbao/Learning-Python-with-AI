# add_10 = lambda x: x + 10
# print(add_10(5))  # Output: 15

# add_two_numbers = lambda a, b: a + b
# print(add_two_numbers(3, 4))  # Output: 7

# numbers = [1, 2, 3, 4]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)  # Output: [1, 4, 9, 16]


# numbers = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)  # Output: [2, 4, 6]

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24