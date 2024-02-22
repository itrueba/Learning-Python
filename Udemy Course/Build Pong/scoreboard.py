from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.hideturtle()
        self.color("White")
        self.speed("fastest")
        self.penup()
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player1_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.player2_score, align=ALIGN, font=FONT)    
        
    def player1_point(self):
        self.player1_score += 1
        self.update()
        
    def player2_point(self):
        self.player2_score += 1
        self.update()

        