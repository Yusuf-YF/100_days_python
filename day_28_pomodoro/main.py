from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#A2DBFA"
PINK = "#F7DAD9"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)


    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=BLUE)

    else:
        count_down(work_sec)
        title_label.config(text="Working", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# window.minsize(width=400, height=500)
window.config(padx=100, pady=112, bg=PINK)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
canvas.pack()
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=PINK, font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=PINK, font=(FONT_NAME, 30, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=PINK, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", bg=PINK, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

check_mark = Label(fg=GREEN, bg=PINK, font=(FONT_NAME, 26))
check_mark.grid(column=1, row=4)

# TODO: fix the bug when start button clicked multiple times.

window.mainloop()
