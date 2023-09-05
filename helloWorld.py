# LEVEL 3, TASK 04 - VERSION CONTROL II: GIT BASICS
# COMPULSORY TASK 01

'''write a program that prints out the message "Hello World!"'''
'''change the message printed out by the program to "Git is awesome!"'''
'''modify your program to accept input from the user and then print out the inputted data'''
'''modify your program to ask the user their name and then print it out'''
'''Change the print feature to print out the following: Hello world, my name is [user's name] and my message is [user's message].'''
# ask for user's name
user_name = input("Please enter your name: \n")
# message
message = input("Enter your message here: \n")
# print out f-string that contains user's name and message
print(f"Hello world, my name is {user_name} and my message is {message}.")