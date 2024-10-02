# # Creating a dictionary
# student = {
#     "name": "Alice",
#     "age": 23,
#     "major": "Computer Science"
# }

# # Accessing values
# print(student["name"])  # Output: Alice
# print(student["age"])   # Output: 23


# Accessing values in a dictionary
student = {
    "name": "Alice",
    "age": 23,
    "major": "Computer Science"
}

# # Accessing the major
major = student["major"]
print(f"Major: {major}")  # Output: Major: Computer Science

# # Using the get() method
age = student.get("age")
print(f"Age: {age}")  # Output: Age: 23

# # If key doesn't exist, return None
grade = student.get("grade")
print(f"Grade: {grade}")  # Output: Grade: None

# # Adding a new key-value pair
student["graduation_year"] = 2025
print(student)

# # Updating an existing key
student["age"] = 24
print(student)


# # Using del
del student["major"]
print(student)

# # Using pop()
age = student.pop("age")
print(f"Removed age: {age}")
print(student)

# # Using popitem()
last_item = student.popitem()
print(f"Removed last item: {last_item}")
print(student)

# Dictionary of a fruit inventory
# fruits = {
#     "apple": 5,
#     "banana": 12,
#     "cherry": 7
# }

# # Loop through keys
# for fruit in fruits:
#     print(f"Fruit: {fruit}")

# # Loop through values
# for count in fruits.values():
#     print(f"Count: {count}")

# # Loop through key-value pairs
# for fruit, count in fruits.items():
#     print(f"There are {count} {fruit}(s).")


student["graduation_year"] = 2025
print(student)
# Using keys(), values(), and items()
print(student.keys())    # Output: dict_keys(['name', 'graduation_year'])
print(student.values())  # Output: dict_values(['Alice', 2025])
print(student.items())   # Output: dict_items([('name', 'Alice'), ('graduation_year', 2025)])

# Using update() to merge dictionaries
student.update({"age": 24, "major": "Physics"})
print(student)

# Clearing the dictionary
student.clear()
print(student)  # Output: {}    