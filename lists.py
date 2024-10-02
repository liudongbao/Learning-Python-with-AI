# # Creating a list
my_list = [1, 2, 3, 4, 5]
# print(my_list)  # Output: [1, 2, 3, 4, 5]

# Accessing elements by index
# print(my_list[0])  # Output: 1
# print(my_list[2])  # Output: 3

# Accessing elements from the end
# print(my_list[-1])  # Output: 5
# print(my_list[-2])  # Output: 4

# Changing the value of an element
my_list[2] = 10
# print(my_list)  # Output: [1, 2, 10, 4, 5]

my_list.append(6)
#print(my_list)  # Output: [1, 2, 10, 4, 5, 6]

# List slicing
#print(my_list[1:3])  # Output: [2, 10] 

# Creating a nested list
# nested_list = [[1, 2], [3, 4], [5, 6]]
# print(nested_list)  # Output: [[1, 2], [3, 4], [5, 6]]

# Iterating over a list
# for item in my_list:
#     print(item)

 # List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]   




