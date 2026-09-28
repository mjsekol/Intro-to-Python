# Functions with Parameters
#? Functions can also take parameters, which are variables that are used to pass information into a function. Parameters allow functions to be more flexible and reusable, as they can perform different tasks based on the input they receive.
#? A value passed through the parameter is called an argument. Arguments are the actual values that are passed to the function when it is called. Parameters are like placeholders for the arguments that will be provided when the function is called.

astronaut_name = input("Welcome astronaut. What is your name? ") # This will prompt the user to input the astronaut's name and store it in astronaut_name
companion_name = input("What is your companion's name? ") # This will prompt the user to input the companion's name and store it in companion_name
def greet_astronaut(astronaut):
    print(f"Hello, {astronaut}! Welcome to the mission.")

greet_astronaut(astronaut_name) # This will call the greet_astronaut function and pass the astronaut_name variable as an argument
greet_astronaut(companion_name) # This will call the greet_astronaut function and pass the companion_name variable as an argument

#! Multiple Parameters
#? Functions can also take multiple parameters, which allows them to accept more than one piece of information. This can be useful for performing more complex tasks or calculations that require multiple inputs.
def greet_all_astronauts(astronaut1, astronaut2):
    print(f"Hello, {astronaut1} and {astronaut2}! Welcome to the mission.")

greet_all_astronauts(astronaut_name, companion_name) # This will call the greet_all_astronauts function and pass both names as arguments    