# exercise 1
fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

# exercise 2
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

# for post in facebook_posts:
#     total_likes = total_likes + post['Likes']

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        post['Likes'] += 0
        # pass

print(total_likes)

# exercise 3 in nato_phonetic_alphabet.py file.

### Error Types ###

# FileNotFound
# with open("file.txt") as file:
#     file.read()

# KeyError
# dict = {"key": "value"}
# value = dict["no_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Exception Handling

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

# BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = round(weight / height ** 2, 2)
print(bmi)
