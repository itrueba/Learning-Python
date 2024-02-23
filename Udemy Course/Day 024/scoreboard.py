from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("White")
        self.speed("fastest")
        self.penup()
        self.goto(0, 260)
        self.update()
        
    def increase(self):
        self.score += 1
        self.update()
        
    def update(self):
        self.clear()
        self.write(f"Score = {self.score} - High Score = {self.high_score}", False, align=ALIGN, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
        
    def game_over(self):
        self.color("Red")
        self.speed("fastest")
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGN, font=FONT)