from turtle import Turtle
import random

RANDOM = range(-280, 280, 20)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        random_x = random.choice(RANDOM)
        random_y = random.choice(RANDOM)
        self.goto(random_x, random_y)
    
    def refresh(self):
        random_x = random.choice(RANDOM)
        random_y = random.choice(RANDOM)
        self.goto(random_x, random_y)