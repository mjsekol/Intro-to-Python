#variable naming
x, y, z = "orange", "banana", "apple" #? This is a multiple assignment of variables

print(x) # This will print the value of the variable x, which is 'orange'
print(y) # This will print the value of the variable y, which is 'banana'
print(z) # This will print the value of the variable z, which is 'apple'

# Input Output... think of text adventure time.
npc_greeting = "Welcome to the world of Python!"
print(npc_greeting) # This will print the NPC's greeting
npc_question = input("What is your name, adventurer? ") # This will prompt the user to input their name
print(f"Hello, {npc_question}! Nice to meet you.") # This will print a personalized greeting
gold_coins = input("How many gold coins do you have? ") # This will prompt the user to input the number of gold coins they have
#you must cross the bridge to get to the other side. The bridge requires a minimum of 1 gold coins to cross.

#! # This will produce error
# npc_troll_collection = (f"The troll collects 1 gold coin from you. You now have {gold_coins - 1} gold coins left.") # This will produce an error because gold_coins is a string and cannot be subtracted from an integer

# We must cast the input to an integer before performing arithmetic operations
gold_coins = float(gold_coins) # This will cast the input to a float

#? Now this won't produce an error because gold_coins is now a float and can be subtracted from an integer
npc_troll_collection = (f"The troll collects 1 gold coin from you. You now have {gold_coins - 1} gold coins left.")
print(npc_troll_collection) # This will print the message about the troll collecting a gold coin and the remaining gold coins





