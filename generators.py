# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# # Using the generator
# counter = count_up_to(5)
# for number in counter:
#     print(number)

# squares = (x * x for x in range(1, 6))

# # Using the generator
# for square in squares:
#     print(square)

def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

# Using the generator
for line in read_large_file('example.txt'):
    print(line)