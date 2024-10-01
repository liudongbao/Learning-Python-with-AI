# Open the file README.md in read mode
with open('README.md', 'r') as file:
    # Loop through each line in the file and print it
    for line in file:
        print(line.strip())
