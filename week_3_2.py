# Functions
# Someone asks for directions to the nearest town. You can create a function that takes the name of the town as a parameter and returns the directions to that town. This way, you can reuse the function for different towns without having to write the directions multiple times.
def get_directions(town_name): #? What's inside the parentheses is a parameter. A parameter is a variable that is used to pass information into a function. In this case, the parameter is town_name, which will be used to pass the name of the town into the get_directions function.
    if town_name.lower() == "springfield": #? This checks if the town name is Springfield (case-insensitive)
        return "Head north for 5 miles, then turn east at the gas station." # This will return the directions to Springfield if the town_name parameter is equal to "springfield" (case-insensitive)
    elif town_name.lower() == "shelbyville":
        return "Take the highway south for 10 miles, then turn west at the old mill."
    else:
        return "Sorry, I don't have directions to that town."

print(get_directions("Springfield")) # This will call the get_directions function and pass "Springfield" as an argument    
print(get_directions("Shelbyville")) # This will call the get_directions function and pass "Shelbyville" as an argument    
print(get_directions("Futurama")) # This will call the get_directions function and pass "Futurama" as an argument    

### SPringfield, spRingfield, SPRINGFIELD, springfield, sPrInGfIeLd, SpRiNgFiElD
# "=" is a command. it is saying something is a value of something else. 
# x = 5 # This assigns the value 5 to the variable x
# x == 5 # This checks if the value of x is equal to 5 and returns True or False
# x != 5 # This checks if the value of x is not equal to 5 and returns True or False