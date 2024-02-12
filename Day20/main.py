from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

is_game_on = True
snake = Snake()

while is_game_on:
    screen.update()
    time.sleep(0.5)
    
    snake.move()

screen.exitonclick()