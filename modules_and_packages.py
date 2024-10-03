# main.py

# Importing the module
# import mymodule
# from mymodule import greet

# print(greet("Bob"))  # Output: Hello, Bob!

# # Using the functions from the module
# print(mymodule.greet("Alice"))  # Output: Hello, Alice!
# print(mymodule.add(5, 3))       # Output: 8

# main.py

# Importing from the package
# from my_package import module1, module2

# # Using functions from the modules inside the package
# print(module1.greet("Charlie"))   # Output: Welcome, Charlie!
# print(module2.multiply(4, 5))     # Output: 20

from my_package.sub_package import module3

print(module3.multiply2(4, 5,2)) 