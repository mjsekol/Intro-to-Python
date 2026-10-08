# Python Dictionaries
# Dictionaries have a Key and Value pair. The key is unique and the value can be of any data type.

student_grades = {
    "John": 85, #key is John and value is 85
    "Jane": 90, #key is Jane and value is 90
    "Bob": 78,  #key is Bob and value is 78
    "Fred": 88, #key is Fred and value is 88
}

print(student_grades) # prints the entire dictionary
print(student_grades["John"]) # prints the grade for John
print(student_grades["Jane"]) # prints the grade for Jane
print(student_grades["Bob"])  # prints the grade for Bob

# Assign a key to a variable and use it to access the value
student_1 = "John"
print(f"Grade for {student_1}: {student_grades[student_1]}") # prints the grade for John using the variable

student_2 = "Jane"
print(f"Grade for {student_2}: {student_grades[student_2]}") # prints the grade for Jane using the variable
student_3 = "Bob"
print(f"Grade for {student_3}: {student_grades[student_3]}") # prints the grade for Bob using the variable

#! What if I have 1000 key:value pairs? It would be tedious to write them all out. Instead, we can use a loop to iterate through the dictionary and print each key and value.
#? Loop is coming up in a very soon Lesson. 

honor_roll_student_grade = student_grades.get("Jane") # assign the value of Jane's grade to a variable    
print(f"Honor roll student: {honor_roll_student_grade}") # prints the grade for Jane using the get() method

# Update the value of John's grade
student_grades["John"] = 95 # updates the value of John's grade to 95
print(f"Updated grade for John: {student_grades['John']}") # prints the

# Delete with pop() method
print(f"Grade for Bob: {student_grades.get('Bob', 'Student not found')}") # prints the grade for Bob or a message if not found
student_grades.pop("Bob") # deletes the key:value pair for Bob
print(f"Grade for Bob: {student_grades.get('Bob', 'Student not found')}") # prints a message if Bob is not found

#Check for a student in the dictionary
if "Jane" in student_grades:
    print(f"Jane's grade is: {student_grades['Jane']}") # prints the grade for Jane if she is in the dictionary
else:
    print("Jane is not in the dictionary") # prints a message if Jane is not in the dictionary

#? You can loop through the dictionary to print all key:value pairs. This will be covered in a future lesson.
for name, grade in student_grades.items():
    print(name, "has a grade of", grade)
