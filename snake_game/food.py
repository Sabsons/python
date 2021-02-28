from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # We can use the turtle class functions directly
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    #Create random food on random coordinates inside the size of the screen
    def refresh(self):
        random_x = random.randint(-280 , 280)
        random_y = random.randint(-280 , 280)
        self.goto(random_x,random_y)
