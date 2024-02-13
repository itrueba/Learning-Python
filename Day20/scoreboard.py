from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("White")
        self.speed("fastest")
        self.penup()
        self.goto(0, 260)
        self.update()
        
    def increase(self):
        self.score += 1
        self.clear()
        self.update()
        
    def update(self):
        self.write(f"Score = {self.score}", False, align=ALIGN, font=FONT)
    
    def game_over(self):
        self.color("Red")
        self.speed("fastest")
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGN, font=FONT)
        