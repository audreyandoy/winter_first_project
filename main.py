# Github
#    - Share projects, can be public or private
# Local vs Remote
#    - Local is stored in computer. Remote.
#    - Why Remote? To share and have access. To keep track of changes and who made them.
# GitIgnore
#    - To hide files from being in the remote version

# name = "Keaton"
# name1 = 123.23
# name2 = True

# Exercise One
# name = input("What is your name?")
# print("Hello {}".format(name))

# Exercise Two
# x = 10
# print(x)

# Exercise Three
# Get user to provide a number.
# Tell user whether that number is:
#     - smaller,
#     - larger,
#     - or equal 10

# num = int(input("Enter a number: "))
# if num > 10:
#     print("The number is greater than 10")
# elif num < 10:
#     print("The number is smaller than 10")
# else:
#     print("The number is equal to 10")

# VARIABLES and CONDITIONALS

#  Exercise Four: Arrays

# my_var = 5
# my_array = ["name", 123, my_var]
# for e in my_array:
#     print(e)

# my_list = [124, 4, 1, 8, 2]
# my_list.sort()
# my_list.append("watermelon")
# print(my_list)

# VARIABLES, CONDITIONALS, LOOPS, AND ARRAYS
# Create an empty array. And fill it with 10 random numbers then print it out

import random
num_array = []
for i in range(10):
    num_array.append(random.randint(1,100))
print(num_array)


