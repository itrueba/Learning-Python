from turtle import Screen, Turtle
import pandas as pd

ALIGN = "center"
FONT = ('Courier', 8, 'normal')

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.setup()

data = pd.read_csv("50_states.csv")

states = data.state.to_list()

while len(states) > 0:
    answer = screen.textinput(f"{50 - len(states)}/50 States Correct", "What is another state name?").title()

    if answer == "Exit":
        new_data = pd.DataFrame(states)
        new_data.to_csv("You Must Study.csv")
        break   
       
    if answer in states:
        state_data = data[data.state == answer]
        state = Turtle()
        state.hideturtle()
        state.penup()
        state.color("Black")
        state.goto(int(state_data.x), int(state_data.y))
        state.write(answer, align=ALIGN, font=FONT)
        states.remove(answer)
