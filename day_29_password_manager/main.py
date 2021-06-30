from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

COLOR = "#C4B6B6"


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


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ops!", message="Please make sure that you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"You have entered:\nWebsite: {website}\n"
                                                                     f"Email/Username: {email}\n"
                                                                     f"Password: {password}\n"
                                                                     f"Are you sure you want to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"Website: {website}, Email/Username: {email}, Password: {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
            messagebox.showinfo(title="Saved", message="Your password information have been saved!")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=COLOR)

canvas = Canvas(height=200, width=200, bg=COLOR, highlightthickness=0)
canvas.pack()
logo = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=COLOR)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=COLOR)
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:", bg=COLOR)
pass_label.grid(column=0, row=3)

website_entry = Entry(width=42)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=42)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

gen_pass = Button(text="Generate Password", width=14, command=generate_password)
gen_pass.grid(column=2, row=3)
add_button = Button(text="Add", width=39, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
