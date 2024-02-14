from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Extra functions

def touch_wall(snake):
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        return 1
    return 0
    
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

is_game_on = False

while not is_game_on:
    speed = int(screen.textinput(title="Choose speed.", prompt="Write one number between 1 (slowest) and 40 (fastest):"))
    if speed > 0 and speed < 41:
        is_game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while is_game_on:
    screen.update()
    time.sleep(1/speed)
    snake.move()
    
    #Detect collisions with food.
    if snake.head.distance(food) < 10:
        snake.extend()
        food.refresh()
        scoreboard.increase()
    
    #Detect collisions with wall.    
    if touch_wall(snake):
        is_game_on = False
        scoreboard.game_over()
        
    #Detect collisions with wall.  
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()