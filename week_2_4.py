# Functions 
# What are functions? Functions are blocks of code that perform a specific task. They can take inputs, called parameters, and can return outputs. Functions help to organize code, make it reusable, and improve readability.
#? Functions are essentially a mini-program within a program. That can be called at any time. Functions can be built-in or user-defined. Built-in functions are provided by Python, while user-defined functions are created by the programmer.
#? Functions can be defined using the def keyword, followed by the function name and parentheses. The code block within every function starts with a colon (:) and is indented.
import time # This will import the time module, which provides various time-related functions

def npc_greeting():    
    print("Welcome to the world of Python!") # This will print the NPC's greeting
    print("What is your name, adventurer?") # This will prompt the user to input their name
    player_name = input() # This will take input from the user and store it in player_name
    print(f"Hello, {player_name}! Nice to meet you.") # This will print a personalized greeting

npc_greeting() # This will call the npc_greeting function and execute the code within it

favorite_food = input("What food do you want to eat? ") # This will prompt the user to input the food they want to eat

#passing through a parameter to a function. A parameter is a variable that is used to pass information into a function. In this case, the parameter is food, which will be used to pass the favorite_food variable into the chef_make_food function.
def chef_make_food(placeholder):
    print(f"Chef is making {placeholder}! It will be ready soon!") # This will print a message indicating the chef is making the requested food
    time.sleep(2) # This will pause the program for 2 seconds to simulate the time taken to make the food
    print(f"Chef has made {placeholder}! Enjoy your meal!") # This will print a message indicating the chef has made the requested food

chef_make_food(favorite_food) # This will call the chef_make_food function and pass the favorite_food variable as an argument

chef_make_food("pizza") # This will call the chef_make_food function and pass the string "pizza" as an argument