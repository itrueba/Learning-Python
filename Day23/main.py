import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create Board
scoreboard = Scoreboard()

# Create Player
player = Player()

# Create Board
car_manager = CarManager()

# Create keyboard listener
screen.listen()
screen.onkey(player.move, "Up")

# Game start
game_is_on = True

while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect Turtle Finish
    if player.is_at_finish_line():
        player.go_to_star()
        car_manager.level_up()
        scoreboard.level_up()
        
    # Detect Turtle collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()   
    

screen.exitonclick()
    