from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ----------------------- CONSTANTS ----------------------- #
BG_COLOR = "#C4B6B6"
GREEN = "#007580"
FONT_NAME = "Microsoft Sans Serif"


# ------------------- PASSWORD GENERATOR ------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    mark = "✔ Copied"
    copy_mark.config(text=mark)


# --------------------- SAVE PASSWORD --------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ops!", message="Please make sure that you haven't left any fields empty.")
    is_ok = messagebox.askokcancel(title="Confirmation", message=f"You have entered:\nWebsite: {website}\n"
                                                                 f"Email/Username: {email}\n"
                                                                 f"Password: {password}\n"
                                                                 f"Are you sure you want to save?")
    if is_ok:
        try:
            with open("data.json", mode="r") as data_file:
                # READING OLD DATA.
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # UPDATING OLD DATA WITH NEW DATA.
            data.update(new_data)

            # SAVING UPDATED DATA.
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            messagebox.showinfo(title="Saved Password", message="Your password information have been saved!")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------- FIND PASSWORD --------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {website} Exists.")


# --------------------- UI SETUP --------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=BG_COLOR)

canvas = Canvas(height=200, width=200, bg=BG_COLOR, highlightthickness=0)
canvas.pack()
logo = PhotoImage(file="logo.png")
canvas.create_image(85, 95, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=BG_COLOR)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=BG_COLOR)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=BG_COLOR)
password_label.grid(column=0, row=3)
copy_mark = Label(fg=GREEN, bg=BG_COLOR, font=(FONT_NAME, 20, "bold"))
copy_mark.grid(column=1, row=5)

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1)
email_entry = Entry(width=42)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

search = Button(text="Search", width=7, command=find_password)
search.grid(column=2, row=1)
gen_pass = Button(text="Generate", width=7, command=generate_password)
gen_pass.grid(column=2, row=3)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

