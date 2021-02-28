from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"Score = {self.score} ", align=ALIGNEMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align=ALIGNEMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

