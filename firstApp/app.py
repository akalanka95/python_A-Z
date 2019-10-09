import math

# print Function
print("Hello ")

# input function
name = input('What is your name? ')
color = input('what\'s your favourite color? ')
print('Hi ' + name + ' ' + color)

# Convert string into int - int()
birth_year = input('Birth Year? ')
age = 2019 - int(birth_year)
print(age)

# Type function
print(type(age))

# More on String
course = 'python\'s course for beginners'

email = '''
thank you 
You are welcome
'''
print(email)

courses = 'Python for beginners'
# Negative charachters
print(courses[3])
print(courses[-2])
print(courses[0:3])
print(courses[0:])
print(courses[:5])

# formatted String
first = 'John'
last = 'smith'
mg = f'{first} {last} is a coder'
print(mg)

# Count the characters
countStr = 'Python for beginners'
print(len(countStr))
countStr.upper()
# No changes to original string
print(countStr.upper())
print(countStr.find('P'))
print(countStr.replace('for', 'no'))
print('Python' in countStr)
print(len(countStr))

x = 2.9
print(round(x))
print(abs(-2.9))

# Math Module
print(math.ceil(2.9))
print(math.floor(2.9))

# If statement
is_hot = True
has_good_income = True
if is_hot and not has_good_income:
    print("It s a hot day ")
else:
    print("Sleep")

i = 1
while i <= 5:
    print(i)
    i += 1











