# class Dog:
#     # Class initializer (constructor) to set up attributes
#     def __init__(self, name, breed, age):
#         self.name = name  # instance attribute
#         self.breed = breed  # instance attribute
#         self.age = age  # instance attribute
    
#     # Method to describe the dog
#     def description(self):
#         return f"{self.name} is a {self.age} years old {self.breed}"
    
#     # Method for dog barking
#     def bark(self):
#         return f"{self.name} says woof!"

# # Creating an object (instance) of the Dog class
# my_dog = Dog("Buddy", "Golden Retriever", 3)

# # Accessing methods and attributes
# print(my_dog.description())  # Output: Buddy is a 3 years old Golden Retriever
# print(my_dog.bark())         # Output: Buddy says woof!

# Parent class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound."

# # Child class inheriting from Animal
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks!"

# # Child class inheriting from Animal
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} meows!"

# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.speak())  # Output: Buddy barks!
# print(cat.speak())  # Output: Whiskers meows!

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age  # Private attribute
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be positive.")

# person = Person("Alice", 30)
# print(person.get_age())  # Output: 30
# person.set_age(35)
# print(person.get_age())  # Output: 35


class Bird:
    def sound(self):
        return "Chirp"

class Duck(Bird):
    def sound(self):
        return "Quack"

class Crow(Bird):
    def sound(self):
        return "Caw"

def make_sound(bird):
    print(bird.sound())

duck = Duck()
crow = Crow()

make_sound(duck)  # Output: Quack
make_sound(crow)  # Output: Caw