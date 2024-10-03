# try:
#     result = 10 / 0
# except:
#     print("An error occurred: division by zero")

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")    

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except Exception as e:
#     print(f"An error occurred: {e}")    


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("This block is executed no matter what.")   
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    else:
        print("Age is valid")

try:
    check_age(167)
except ValueError as e:
    print(f"An error occurred: {e}")    