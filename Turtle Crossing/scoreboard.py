from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(300,300)
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-270,250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def new_level_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align="center", font=FONT)