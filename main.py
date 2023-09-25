import turtle

import pandas
from turtle import Turtle
from turtle import Screen

screen = Screen()
screen.title("U.S. States game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
file_path = "50_states.csv"

data = pandas.read_csv(file_path)
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        zaki = Turtle()
        zaki.hideturtle()
        zaki.penup()
        state_data = data[data["state"] == answer_state]
        zaki.goto(int(state_data["x"]), int(state_data["y"]))
        zaki.pendown()
        zaki.write(answer_state)

    elif answer_state == "exit" or answer_state == "Exit":
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("States to Learn.csv")
        break
    else:
        print(f"{answer_state} is not a state.")

