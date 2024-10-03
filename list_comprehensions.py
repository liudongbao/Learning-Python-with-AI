# Creating a list of squares of numbers from 0 to 9
# squares = [x**2 for x in range(10)]
# print(squares)


# Creating a list of even numbers from 0 to 9
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)

# Creating a list of tuples (x, y) for x in range(3) and y in range(3)
# pairs = [(x, y) for x in range(3) for y in range(3)]
# print(pairs)

# Applying a function to each element in the list
# def square(x):
#     return x**2

# squared_list = [square(x) for x in range(5)]
# print(squared_list)

# Flattening a 2D list into a 1D list
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_list = [item for sublist in matrix for item in sublist]
# print(flat_list)

# Creating a list of numbers divisible by both 2 and 3
divisible_by_2_and_3 = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
print(divisible_by_2_and_3)