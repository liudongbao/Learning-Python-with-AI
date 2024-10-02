# # Example 1: Creating a set
# my_set = {1, 2, 3, 4, 5}
# print(my_set)

# # Example 2: Using set() to create a set
# another_set = set([1, 2, 3, 4])
# print(another_set)

# # Adding elements to a set
# my_set.add(6)
# print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# # Removing elements from a set
# my_set.remove(3)
# print(my_set)  # Output: {1, 2, 4, 5, 6}

# # Using discard (it does not raise an error if the element doesn't exist)
# my_set.discard(10)  # No error, even though 10 is not in the set

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1 & set2  # or set1.intersection(set2)
print(intersection_set)  # Output: {3}

difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)  # Output: {1, 2}

sym_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 2, 4, 5}


# Removing duplicates using a set
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)  # Convert to set to remove duplicates
unique_list = list(my_set)  # Convert back to list
print(unique_list)  # Output: [1, 2, 3, 4, 5]