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
#   elif num2 >= num1 and num2 >= num3:
#     return num2
#   else:
#     return num3
# print(max_num(1,2,3))