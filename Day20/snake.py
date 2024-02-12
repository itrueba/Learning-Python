from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
            
    def create_snake(self):
        for position in STARTING_POSITIONS:
            part = Turtle(shape="square")
            part.color("white")
            part.penup()
            part.goto(position)
            self.parts.append(part)
            
    def move(self):
        for num in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[num - 1].xcor()
            new_y = self.parts[num - 1].ycor()
            self.parts[num].goto(new_x, new_y)
        self.parts[0].forward(MOVE_DISTANCE)