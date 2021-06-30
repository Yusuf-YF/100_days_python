from tkinter import *


def action():
    miles = float(miles_input.get())
    km = round(miles * 1.609344, 2)
    km_result.config(text=km)


window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=200)
window.config(bg="gray")
window.config(padx=90, pady=50)

miles_input = Entry(width=5)
miles_input.config(bg="gray")
miles_input.insert(END, string=0)
miles_input.grid(column=2, row=0)

miles_label = Label(text="Miles")
miles_label.config(bg="gray")
miles_label.grid(column=3, row=0)

equal_label = Label(text="is equal to:")
equal_label.config(bg="gray")
equal_label.grid(column=0, row=1)

km_result = Label(text=0)
km_result.config(bg="gray")
km_result.grid(column=2, row=1)

km_label = Label(text="KM")
km_label.config(bg="gray")
km_label.grid(column=3, row=1)

button = Button(text="Calculate", command=action)
button.config(bg="gray")
button.grid(column=2, row=3)

window.mainloop()
