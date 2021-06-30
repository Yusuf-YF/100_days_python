import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# prompt user to enter a valid input with while loop.
# is_correct = True
# while is_correct:
#     word = input("Enter a word: ").upper()
#     if len(word) == 0:
#         print("Please enter a word.")
#     else:
#         try:
#             output_list = [phonetic_dict[letter] for letter in word]
#         except KeyError:
#             print("Sorry, only letters in the alphabet please.")
#         else:
#             print(output_list)

# prompt user to enter a valid input with a function.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    if len(word) == 0:
        print("Please enter a valid input.")
        generate_phonetic()
    else:
        try:
            output_list = [phonetic_dict[letter] for letter in word]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
            generate_phonetic()
        else:
            print(output_list)


generate_phonetic()
