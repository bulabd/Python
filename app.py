####### BASICS #######
# print("Hello World!")
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")


####### VARIABLES #######
# a_variable = "Bulat"
# age = 20
# is_male = True
# print("Hello " + a_variable + ", you are " + str(age) + " years old")


####### WORKING WITH STRINGS #######
# print('Giraffe "Academy"')
# print("Giraffe\"Academy")
# print("Giraffe\\Academy")
# phrase = 'Giraffe Academy'
# print(len(phrase.upper()))
# print(phrase[8])
# print(phrase.index('z'))
# print(phrase.replace("Giraffe", "Lion"))

####### WORKING WITH NUMBERS #######
# print(3 + 5.09)
# print(3 * (4 + 5))
# print(12 % 5)
# my_num = -7
# print(str(my_num) + " is a number")
# print(abs(my_num))
# print(pow(my_num, 2))
# print(max(5, 20))
# print(min(20, 1))
# print(round(3.72232))
from math import *
# print(floor(4.99))
# print(ceil(3.1))
# print(sqrt(36))

####### GET INPUT FROM USER #######
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age + " years old!")

####### BASIC CALCULATOR #######
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

####### MAD LIBS GAME #######
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are {color}".format(color=color))
# print("{plural_noun} are blue".format(plural_noun = plural_noun))
# print("I love {celebrity}".format(celebrity = celebrity))

####### LISTS (Arrays) #######
# list = ["Bob", "Man", "Bruh", "OK", 20, 22, 1, 54, True, False]
# list[1] = "Bulat"
# print(list[-3])
# print(list[1:3])
# print(list[1])

####### LIST FUNCTIONS #######
# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ["Bob", "Joe", "John", "Riddler"]
# friends.extend(lucky_numbers)
# friends.append(45555)
# friends.insert(1, "Bulat")
# print(friends)

####### TUPLES #######
# coordinates = (4, 5)
# coordinates[1] = 10  --------> error cannot modify tupple
# print(coordinates[0])

####### FUNCTIONS #######
# def say_hi(name, age):
#   print("Hello " + name + " you are " + age)
# say_hi("Bulat", "20")

####### RETURN STATEMENT #######
# def cube(num):
#   return  num ** 3
# print(cube(2))

####### IF STATEMENTS #######
# is_male = True
# is_tall = False
# if is_male and is_tall:
#   print("You are a male or tall or both")
# elif is_male and not(is_tall):
#   print("You are a not tall male")
# else:
#   print("You are not a male nor tall")

####### IF STATEMENTS AND COMPARISONS #######
# def max_num(num1, num2, num3):
#   if num1 >= num2 and num1 >= num3:
#     return num1
#   elif num2 != num1 and num2 >= num3:
#     return num2
#   else:
#     return num3
# print(max_num(1,2,3))
# <= >= !=

####### BUILDING A BETTER CALCULATOR #######
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
# if op == "+":
#   print(num1 + num2)
# elif op == "-":
#   print(num1 - num2)
# elif op == "/":
#   print(num1 / num2)
# elif op == "*":
#   print(num1 * num2)
# else:
#   print("Invalid operator")

####### DICTIONARIES (object) #######
# monthConversion = {
#   "Jan": "January",
#   "Feb": "February",
#   "Mar": "March",
#   "Apr": "April",
#   "Jun": "June",
#   "Jul": "July",
#   "Aug": "August",
#   "Sep": "September",
#   "Oct": "October",
#   "Nov": "November",
#   12: "December"
# }
# print(monthConversion["Nov"])
# print(monthConversion.get("Nov"))
# print(monthConversion.get("BRUH", "Not a valid key"))
# print(monthConversion[12])

####### WHILE LOOP #######
# i = 1
# while i <= 10:
#   print(i)
#   i += 1
#
# print("done with loop")

####### GUESSING GAME #######
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not out_of_guesses:
#   if guess_count < guess_limit:
#     guess = input("Enter guess: ")
#     guess_count += 1
#   else:
#     out_of_guesses = True
#
# if out_of_guesses:
#   print("You are out of guesses!")
# else:
#   print("You guessed the secret word giraffe!")

####### FOR LOOP #######
# friends = ["A", "B", "C", "D"]
# for friend in range(len(friends)):
#   print(friend.__index__())

####### EXPONENT FUNCTION #######
# # print(2 ** 3)
# def raise_to_power(base_number, power_number):
#   result = 1
#   for index in range(power_number):
#     result *= base_number
#   return result
#
# print(raise_to_power(2, 4))

####### 2D LIST AND NESTED LOOPS #######
# number_grid = [
#   [1, 2, 3, 4],
#   [5, 6, 7],
#   [8, 9],
#   [0]
# ]
# print(number_grid[0][1])
# for list in number_grid:
#   for number in list:
#     print(number)

####### BUILD A TRANSLATOR #######
# def translate(phrase):
#   translated_phrase = ""
#   for letter in phrase:
#     if letter.lower() in "aeiou":
#       if letter.isupper():
#         translated_phrase += "G"
#       else:
#         translated_phrase += "g"
#     else:
#       translated_phrase += letter
#   return translated_phrase
# print(translate(input("Enter a phrase: ")))

####### COMMENTS #######
# This is a comment
# '''
# multiple line comment
# '''
# print('haha')

####### TRY/EXCEPT #######
# try:
#   value = 10/0
#   number = int(input("Enter a number: "))
#   print(number)
# except ZeroDivisionError as err:
#   print(err)
# except ValueError:
#   print("Invalid input")

####### READING FILES #######
# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#   print(employee)
# # print(employee_file.readlines()[1])
# employee_file.close()

####### WRITING TO FILES #######
# employee_file = open("employees.txt", "a") # "r" or "a" or "w"
# employee_file.write("\nToby - Human Resources")
# employee_file.close()

####### MODULES AND PIP #######
# import useful_tools
# print(useful_tools.roll_dice(10))
# pip



