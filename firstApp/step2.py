guess_count = 1
while guess_count <= 5:
    print('*' * guess_count)
    guess_count += 1

# Guess the number
win_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_number = int(input("Guess: "))
    guess_count += 1
    if guess_number == win_number:
        print("You WON")
        break
else:
    print("Sorry Man You LOSS.")

# Car Game
command = ''

while True:
    command = input('> ').lower()
    if command == 'start':
        print("Car started...")
    elif command == 'quit':
        break
    else:
        print('Sorry I don\'t understand')


# For loops
for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Sera']:
    print(item)

for item in range(10):
    print(item)

# range(5, 20)
# range (5, 20, 2)

# Nested Loops
for x in range(4):
    for y in range(4):
        print(f'({x},{y})')

numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print('X' * item)

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

number_list = [1, 2, 3, 4, 5, 6, 13, 5]
number_list.append(23)
number_list.insert(0, 29)
number_list.remove(4)
number_list.pop()
# number_list.clear()
number_list.index(5)
print(50 in number_list)
number_list.count(5)
number_list.sort()
print(number_list)
number_list.reverse()
# Get the copy of the first list
number_list2 = number_list.copy()

print('Duplicate List')

# Remove Duplicate items from a list
duplicate_list = [2, 4, 2, 5, 4, 8, 4, 4]
unique_list = []
for number in duplicate_list:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)

# Tuples
# tuples Are immutable
tuples_list = (1, 2, 3)  # This is a tuple

# Unpacking
coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
x, y, z = coordinates  # This is unpacking

# Dictionaries
customer = {
    "name": "John",
    "age": 30,
    "is_verified": True
}
print(customer['name'])  # Pass a error if ot present
print(customer.get('name'))  # Didn't give a error if not present

# adding a new value
customer["birthday"] = "1998 of july"

# Phone number exercise
phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

# Emoji Convertor
message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😂"
}

outputs = ""
for word in words:
    outputs += emojis.get(word, word) + ' '
print(outputs)

