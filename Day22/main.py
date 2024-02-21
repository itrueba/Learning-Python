from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

import time

# Create Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

# Create Paddles for Players
player1 = Paddle(position = (-350, 0))
player2 = Paddle(position = (350, 0))

# Create Ball
ball = Ball()

# Create Scoreboard
scoreboard = Scoreboard()

# Create keyboard listener
screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

# Start Game
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision whit wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect collision whit paddle
    if ball.distance(player1) < 50 and ball.xcor() < -320 or ball.distance(player2) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    
    # Detect Player1 misses 
    if ball.xcor() < -380:
        scoreboard.player2_point()
        ball.reset_position()
        
    # Detect Player2 misses    
    if ball.xcor() > 380:
        scoreboard.player1_point()
        ball.reset_position()
        
screen.exitonclick()