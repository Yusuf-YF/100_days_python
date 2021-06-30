# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()
    print(letter)

with open("Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
    print(names)

    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]", stripped_name)
        print(new_letter)

        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as send_file:
            send_file.write(new_letter)
