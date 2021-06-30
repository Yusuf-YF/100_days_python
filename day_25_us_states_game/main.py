import turtle
import pandas

screen = turtle.Screen()

screen.setup(width=730, height=500)
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get mouse x and y coordinates.
# def mouse_click_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(mouse_click_cor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# print(all_states)
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                             prompt="What's another state name?").title()
    if guess == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif guess in all_states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)

