from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500 ,height=400)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [80, 50, 20, -10, -40, -70]
turtle_list = []

while not is_race_on:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
    if user_bet in colors:
        is_race_on = True

for index in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.shape("turtle")
    new_turtle.goto(-230, y_positions[index])
    turtle_list.append(new_turtle)
    

    
while is_race_on:
    for turtle in turtle_list:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You have won! The {winner} turtle is the winner!")
            else:
                print(f"You have lost! The {winner} turtle is the winner!")
            is_race_on = False



screen.exitonclick()