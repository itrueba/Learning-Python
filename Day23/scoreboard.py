from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update()
            
    def level_up(self):
        self.level += 1
        self.clear()
        self.update()
    
    def update(self):
        self.write(f"Level = {self.level}", False, align=ALIGN, font=FONT)
        
    def game_over(self):
        self.color("Red")
        self.speed("fastest")
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGN, font=FONT)
