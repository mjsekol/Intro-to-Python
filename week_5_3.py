# Control Flow
# Boolean = True or False
# Control flow checks for conditions and executes code based on those conditions... it checks for true or false, if true it executes something.

# lightsaber_skill = 50

lightsaber_skill = int(input("Enter your lightsaber skill level (0-100): "))

if lightsaber_skill >= 90:
    print("You are a Jedi Master!")
elif lightsaber_skill >= 70:
    print("You are a Jedi Knight.")
elif lightsaber_skill >= 40:
    print("You are a Padawan.")
elif lightsaber_skill >= 20:
    print("You are a Youngling.")
else:
    print("You need more practice.")

