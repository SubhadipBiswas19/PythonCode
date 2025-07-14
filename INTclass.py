# #Create variables for name, age, and salary, and print them.
# # Define variables
# name = "Subhadip"
# age = 35
# salary = 100.99
#
# # Print the variables
# print("Name:", name)
# print("Age:", age)
# print("Salary:", salary)
#
# print("============================================================")
# #Make a dictionary with keys name, age, skills (list). Print types of all values.
# # Define the dictionary
# person = {
#     "name": "Alice",
#     "age": 30,
#     "skills": ["Python", "Selenium", "SQL"]
# }
#
# # Print the types of all values
# print("Type of 'name':", type(person["name"]))
# print("Type of 'age':", type(person["age"]))
# print("Type of 'skills':", type(person["skills"]))
#
# print("============================================================")
# #Convert float to int and string to int; print results.
# # Float to int
# my_float = 12.75
# int_from_float = int(my_float)
# print("Float to int:", int_from_float)
#
# # String to int
# my_string = "100"
# int_from_string = int(my_string)
# print("String to int:", int_from_string)
#
# print("============================================================")
# #Write a function that checks if input is int or str and returns a message.
# def check_type(value):
#     if isinstance(value, int):
#         return "The input is an integer."
#     elif isinstance(value, str):
#         return "The input is a string."
#     else:
#         return "The input is neither an integer nor a string."
#
# print(check_type(42))
# print(check_type("Hello"))
# print(check_type(3.14))
#
# print("============================================================")
# def check_input_type(value):
#     if isinstance(value, int):
#         return "The input is an integer."
#     elif isinstance(value, str):
#         return "The input is a string."
#     else:
#         return "The input is of unknown type."
#
# # Take user input
# user_input = input("Enter something: ")
#
# # Try to convert to int first
# try:
#     converted_input = int(user_input)
# except ValueError:
#     converted_input = user_input
#
# # Pass to function and print result
# result = check_input_type(converted_input)
# print(result)
#
# print("============================================================")
# #Compare two numbers and print which is greater.
# # Input two numbers from the user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
#
# # Compare and print result
# if num1 > num2:
#     print("First number is greater.")
# elif num2 > num1:
#     print("Second number is greater.")
# else:
#     print("Both numbers are equal.")
#
# print("============================================================")
# #Calculate the area of a rectangle using arithmetic operators.
# # Input length and width from the user
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
#
# # Calculate area using arithmetic multiplication (*)
# area = length * width
#
# # Print the result
# print("The area of the rectangle is:", area)
#
# print("============================================================")
# #Check if a person’s age is between 18 and 60 using logical operators.
# # Take age input from the user
# age = int(input("Enter your age: "))
#
# # Check if age is between 18 and 60 using logical AND
# if age >= 18 and age <= 60:
#     print("Age is between 18 and 60.")
# else:
#     print("Age is not in the range 18 to 60.")
#
# print("============================================================")
# #Concatenate two strings and print the result.
# # Take two string inputs
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
#
# # Concatenate using +
# result = str1 + str2
#
# # Print the result
# print("Concatenated string:", result)
from code import interact

# print("============================================================")
# #Add and remove elements from a list.
# fruits = ['Apple','Banana','Grapefruit']
#
# fruits.append('Orange')
# fruits.insert(4,'Watermelon')
# fruits.extend(['Mango'])
# print(fruits)
#
# fruits.remove('Mango')
# fruits.pop(4)
# del fruits[3]
# print(fruits)

# print("============================================================")
# #Print all keys and values of a dictionary.
# employee = {"name": "Alice","age": 30,"city": "New York"}
#
# for key, value in employee.items():
#     print(f"{key}: {value}")
#
# print("============================================================")
# #Use map to square numbers in a list.
# numbers = [1, 2, 3, 4, 5]
#
# squared_numbers = list(map(lambda x: x ** 2, numbers))
#
# print(squared_numbers)
#
# print("============================================================")
# #Perform union and intersection of two sets.
# name1 = {'Subhadip','Bose', 'Subham','Sen' }
# name2 = {'Rahul','Roy','Subhadip','Roy'}
#
# unionname= name1.union(name2)
# intersectionname= name1.intersection(name2)
#
# print(unionname)
# print(intersectionname)
# print("============================================================")
# #Create a tuple and try to modify it (check immutability).
# my_tuple = (10, 20, 30)
# my_tuple[1] = 99
# print(my_tuple)

# print("============================================================")
# #Create a list of squares of numbers 1-5 using list comprehension.
# result = [x**2 for x in range(1,6)]
# print(result)

# print("============================================================")
# #Create a dict where keys are numbers 1-3 and values are their squares.
# result = {x: x**2 for x in range(1, 4)}
# print(result)
#
# print("============================================================")
# #Create a set of even numbers from 1-10 using comprehension.
# result = {x for x in range(1, 11) if x % 2 == 0}
# print(result)

# print("============================================================")
# #Slice a string and print the first three characters.
# text = "Subhadip"
# result = text[:3]
# print(result)

# print("============================================================")
# #Format a string using f-string with name and age.
# name = "Subhadip"
# age = 35
#
# result = f"My name is {name} and I am {age} years old."
# print(result)
#
# print("============================================================")
# name = "Subhadip"
# salary = 50
#
# result = "Employee Name: {} and Salary: INR {}".format(name, salary)
# print(result)

# print("============================================================")
# #Take input for name and print a greeting.
# name = input("Enter your name: ")
# print(f"Hello, {name} Welcome!")

# print("============================================================")
# #Create a class Car with attributes brand, model.
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def display_info(self):
#         print(f"Car Info: {self.brand} {self.model} ")
#
# my_car = Car("Toyota", "Camry")
# my_car.display_info()

# print("============================================================")
#Create an object of Car and print its attributes.
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
# my_car = Car("Toyota", "Camry", 2022)
#
# print("Brand:", my_car.brand)
# print("Model:", my_car.model)
# print("Year:", my_car.year)

# print("============================================================")
#Use @classmethod to print class-level info.
# class Student:
#     # Class variable
#     school_name = "Green Valley High School"
#
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Grade: {self.grade}")
#
#     @classmethod
#     def show_school(cls):
#         print(f"School Name: {cls.school_name}")
#
# s1 = Student("Aarav", "8th")
# s2 = Student("Priya", "9th")
#
# s1.display_info()
# s2.display_info()
# s2.show_school()

# print("============================================================")
#Use @staticmethod to print a static message.
# class Student:
#     @staticmethod
#     def welcome_message():
#         print("Welcome to Green Valley High School!")
#
# Student.welcome_message()
#
# s1=Student()
# s1.welcome_message()

# print("============================================================")
#Create a subclass ElectricCar that inherits from Car.
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, year, battery_capacity):
#         super().__init__(brand, model, year)
#         self.battery_capacity = battery_capacity
#
#     def display_battery(self):
#         print(f"Battery Capacity: {self.battery_capacity} kWh")
#
#
# e_car = ElectricCar("Tesla", "Model Y", 2025, 85)
#
# e_car.display_info()
# e_car.display_battery()

# print("============================================================")
#Override a method in ElectricCar.
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, year, battery_capacity):
#         super().__init__(brand, model, year)
#         self.battery_capacity = battery_capacity
#
#
#     def display_info(self):
#         super().display_info()  # Optionally call the base version
#         print(f"Battery Capacity: {self.battery_capacity} kWh")
#
#
# e_car = ElectricCar("Tesla", "Model X", 2024, 100)
#
# e_car.display_info()

#print("============================================================")
#Demonstrate protected member _mileage.
# class Car:
#     def __init__(self, brand, model, year, mileage):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self._mileage = mileage  # Protected member
#
#     def display_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
#         print(f"Mileage (inside Car): {self._mileage} km/l")
#
# class ElectricCar(Car):
#     def display_battery_and_mileage(self, battery_capacity):
#         print(f"Battery Capacity: {battery_capacity} kWh")
#         print(f"Mileage (accessed in ElectricCar): {self._mileage} km/l")
#
# e_car = ElectricCar("Tesla", "Model 3", 2023, 400)
#
#
# e_car.display_info()
# e_car.display_battery_and_mileage(75)

#print("============================================================")
#Import math module and print square root of a number.
# import math
# num = 25
# sqrt_value = math.sqrt(num)
# print(f"The square root of {num} is {sqrt_value}")

# print("============================================================")
#Import sqrt from math and use it.
# from math import sqrt
# num = 36
# result = sqrt(num)
# print(f"The square root of {num} is {result}")

#print("============================================================")
#Write a generator that yields numbers 1 to 5.
# def number_generator():
#     for i in range(1, 6):
#         yield i
#
# gen = number_generator()
# for num in gen:
#     print(num)

#print("============================================================")
#Write text to a file and read it back.
# with open("sample.txt", "w") as file:
#     file.write("Hello, this is a sample file.\n")
#     file.write("Written using Python file handling.")
#
#
# with open("sample.txt", "r") as file:
#     content = file.read()
#
# print("File Content:\n", content)

#print("============================================================")
#Read a file line by line.
# with open("sample.txt", "r") as file:
#     for line in file:
#         print(line.strip())

#print("============================================================")
#Append a line to an existing file.
# with open("sample.txt", "a") as file:
#     file.write("\nThis line was appended.")
#
# print("Line appended successfully.")

#print("============================================================")
#Use os to list files in a directory.
# import os
#
# items = os.listdir(".")
#
# for item in items:
#     print(item)

#print("============================================================")
#Use sys to print Python version.
# import sys
#
# print("Full Python version info:", sys.version)
#
# print("Python version:", sys.version_info.major, sys.version_info.minor, sys.version_info.micro)

#print("============================================================")
#Use datetime to print current date and time.
# from datetime import datetime
#
# now = datetime.now()
#
# print("Current date and time:", now)

#print("============================================================")
#Use time.sleep() to pause for 2 seconds.
# import time
#
# print("Waiting for 2 seconds...")
# time.sleep(2)
# print("Resumed after 2 seconds!")

# print("============================================================")
# #Use filter to keep only even numbers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#
# print("Even numbers:", even_numbers)

# print("============================================================")
# #Use reduce to compute the product of numbers in a list.
# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
#
# product = reduce(lambda x, y: x * y, numbers)
#
# print("Product of numbers:", product)

# print("============================================================")
# #Write a function that returns the square of a number.
# def square(num):
#     return num ** 2
#
# result = square(5)
# print("Square of 5 is:", result)

# print("============================================================")
# #Write a function that takes name and age as positional arguments and prints them.
# def display_info(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#
# display_info("Subhadip", 35)

# print("============================================================")
# #Write a function with a default parameter country="India".
# def greet(name, country="India"):
#     print(f"Hello, {name} from {country}!")
#
# greet("Subhadip")
# greet("Subham", "USA")

# print("============================================================")
# #Check if a file exists using os.path.
# import os
#
# filename = "sample.txt"
#
# if os.path.exists(filename):
#     print(f"File '{filename}' exists.")
# else:
#     print(f"File '{filename}' does not exist.")

# print("============================================================")
# #Use pathlib to get file name and extension.
# from pathlib import Path
#
# # Create a Path object
# file_path = Path("example_folder/sample.txt")
#
# file_name = file_path.name
#
# file_extension = file_path.suffix
#
# print("File name:", file_name)
# print("File extension:", file_extension)

print("============================================================")
#Write a program to check if a number is positive, negative, or zero.
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("============================================================")
