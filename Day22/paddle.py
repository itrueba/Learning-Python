from turtle import Turtle

MOVE_SPEED = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("White")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)        
    
    def up(self):
        new_y = self.ycor() + MOVE_SPEED
        self.goto(x = self.xcor(), y=new_y)
        
    def down(self):
        new_y = self.ycor() - MOVE_SPEED
        self.goto(x = self.xcor(), y=new_y)