# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like!? \n"))
num_symbols = int(input("How many symbols would you like!? \n"))
num_numbers = int(input("How many numbers would you like!? \n"))

# EASY LEVEL

# password = ""

# for char in range(1, num_letters + 1):
#     password += random.choice(letters)
# # print(password)

# for char in range(1, num_numbers + 1):
#     password += random.choice(numbers)
# # print(password)

# for char in range(1, num_symbols + 1):
#     password += random.choice(symbols)
# print(f"Your password is: \n{password}")

# HARD LEVEL


password_list = []

for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

# show the password as a string
password = ""

for char in password_list:
    password += char

print(f"Your password is: \n{password}")
