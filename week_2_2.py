#DataType Casting
#? Input from the terminal is always a string. So, we need to cast it to the required data type.
number1 = input("Enter a number: ") #? This will take input from the user and store it in number1 as a string
print(type(number1)) #? This will print the data type of number1

number2 = input("Enter another number: ") #? This will take input from the user, cast it to a float and store it in number2
print(type(number2)) #? This will print the data type of number2

print(number1 + number2) #? This will print the concatenation of number1 and number2 as strings

# Convert string to float.
number1 = float(number1)
number2 = float(number2)
print(type(number1), type(number2)) #? This will print the data type of number1 and number2  after casting to float

print(number1 + number2) #? This will print the sum of number1 and number2 as floats