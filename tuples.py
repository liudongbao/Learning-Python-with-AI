# Creating a tuple with multiple elements
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Tuple with different types of elements
# mixed_tuple = (1, "apple", 3.14, True)
# print(mixed_tuple)  # Output: (1, 'apple', 3.14, True)

# Tuple with one element
# single_element_tuple = (5,)
# print(single_element_tuple)  # Output: (5,)

# my_tuple = ('a', 'b', 'c', 'd')

# # Access the first element
# print(my_tuple[0])  # Output: 'a'

# # Access the last element
# print(my_tuple[-1])  # Output: 'd'

# my_tuple = (10, 20, 30, 40, 50)

# # Slice from index 1 to 3 (not inclusive of 3)
# print(my_tuple[1:3])  # Output: (20, 30)

# # Slice from the beginning to index 3
# print(my_tuple[:3])  # Output: (10, 20, 30)

# # Slice from index 2 to the end
# print(my_tuple[2:])  # Output: (30, 40, 50)

# my_tuple = (1, 2, 3)

# # Trying to change the value at index 0
# my_tuple[0] = 10  # Raises TypeError: 'tuple' object does not support item assignment

# my_tuple = (1, 2, 3, 2, 4, 2)

# # Count occurrences of 2
# print(my_tuple.count(2))  # Output: 3

# # Find index of first occurrence of 3
# print(my_tuple.index(3))  # Output: 2

# # Packing values into a tuple
# packed_tuple = 1, 2, 3
# print(packed_tuple)  # Output: (1, 2, 3)

# # Unpacking the tuple into variables
# a, b, c = packed_tuple
# print(a)  # Output: 1
# print(b)  # Output: 2
# print(c)  # Output: 3

# Dictionary with a tuple as a key
my_dict = {('x', 'y'): "Point XY", (1, 2): "Coordinates"}
print(my_dict)  # Output: {('x', 'y'): 'Point XY', (1, 2): 'Coordinates'}