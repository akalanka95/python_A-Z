# Functions in Python
def greet_user(name):
    print(f'Hi there! {name}')
    print('Welcome.......')


print("Start")
greet_user('John')

# Exceptions
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age can not be Zero')
except ValueError:
    print('Invalid Value')




