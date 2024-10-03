# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello!")

# # When you call say_hello(), it will include the behavior of the decorator.
# say_hello()


# import time

# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)  # Call the original function
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time:.4f} seconds")
#         return result
#     return wrapper

# @timing_decorator
# def compute_square(n):
#     time.sleep(1)  # Simulate a time-consuming task
#     return n * n

# result = compute_square(4)
# print(f"Result: {result}")


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")