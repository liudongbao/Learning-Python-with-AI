# Creating strings
# single_quote_string = 'Hello'
# double_quote_string = "World"
# multi_line_string = '''This is a 
# multi-line string'''

# print(single_quote_string)  # Output: Hello
# print(double_quote_string)  # Output: World
# print(multi_line_string)    # Output: This is a 
#                             #         multi-line string

# greeting = single_quote_string + ' ' + double_quote_string
# print(greeting)  # Output: Hello World                            

# repeat_str = "Ha" * 3
# print(repeat_str)  # Output: HaHaHa


# word = "Python"
# # Accessing characters by index
# print(word[0])  # Output: P (First character)
# print(word[-1]) # Output: n (Last character)

# # Slicing a string
# print(word[0:3])  # Output: Pyt (Characters from index 0 to 2)
# print(word[1:])   # Output: ython (From index 1 to end)
# print(word[:4])   # Output: Pyth (From start to index 3)

# word = "Python"
# # Changing the first letter to 'J'
# new_word = 'J' + word[1:]
# print(new_word)  # Output: Jython


# text = "Hello, Python!"
# print(text.lower())  # Output: hello, python!
# print(text.upper())  # Output: HELLO, PYTHON!

# text = "I love Python"
# new_text = text.replace("Python", "coding")
# print(new_text)  # Output: I love coding

# text = "   Hello, World!   "
# print(text.strip())  # Output: Hello, World!

# text = "apple,banana,cherry"
# fruit_list = text.split(',')
# print(fruit_list)  # Output: ['apple', 'banana', 'cherry']

# fruits = ['apple', 'banana', 'cherry']
# fruits_string = ', '.join(fruits)
# #print(fruits_string)  # Output: apple, banana, cherry

# name = "Alice"
# age = 25
# info = f"My name is {name} and I am {age} years old."
# print(info)  # Output: My name is Alice and I am 25 years old.

# sentence = "Python is fun"
# print("Python" in sentence)  # Output: True
# print("Java" in sentence)    # Output: False

# sentence = "Python is awesome"
# index = sentence.find("is")
# print(index)  # Output: 7

# text = "Python"
# reversed_text = text[::-1]
# print(reversed_text)  # Output: nohtyP

quote = 'He said, "Python is amazing!"'
newline_example = "First Line\nSecond Line"
tab_example = "Column1\tColumn2"

print(quote)           # Output: He said, "Python is amazing!"
print(newline_example) # Output: First Line
                       #         Second Line
print(tab_example)     # Output: Column1  Column2