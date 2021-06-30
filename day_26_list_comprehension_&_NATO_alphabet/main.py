student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# LOOP THROUGH A DATA FRAME
for (key, value) in student_data_frame.items():
    pass

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        pass

for (index, row) in student_data_frame.iterrows():
    # Access index and row
    if row.student == "Lily":
        pass
    # Access row.student or row.score
    if row.student == "James":
        pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# df = pandas.DataFrame(data)
# print(df)
phonetic = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic)
# {new_key:new_value for (letter, code) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
new_word = [phonetic[letter] for letter in word]
print(new_word)
