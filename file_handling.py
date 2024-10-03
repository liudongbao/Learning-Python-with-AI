# # Opening a file
# file = open('example.txt', 'w')  # Opens in write mode

# # Writing to the file
# file.write("Hello, Python file handling!")

# # Closing the file
# file.close()

# file = open('example.txt', 'a')  # Opens in append mode

# file.write("\nAdding a new line to the file.")
# file.write("\nAnd another one.")

# file.close()  # Always remember to close the file

# file = open('example.txt', 'r')  # Opens in read mode

# content = file.read()  # Reads the entire file content
# print(content)

# file.close()

# file = open('example.txt', 'r')

# line = file.readline()  # Reads the first line
# print(line)

# file.close()

# file = open('example.txt', 'r')

# lines = file.readlines()  # Reads all lines into a list
# for line in lines:
#     print(line)

# file.close()

# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)


try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")   