# Open the file in read mode
with open('README.md', 'r') as file:
    # Read the file line by line
    for line in file:
        # Output each line
        print(line.strip())