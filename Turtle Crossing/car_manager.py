from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    car_list = []
    number_list = [1,2,3,4,5]


    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(300,300)
        self.speed = STARTING_MOVE_DISTANCE
    def createCar(self):
        if random.choice(self.number_list) == 3:
            tim = Turtle(shape="square")
            tim.color(random.choice(COLORS))
            tim.shapesize(stretch_wid=2,stretch_len=1)
            tim.penup()
            tim.goto(270,random.randint(-230,230))
            tim.left(90)
            self.car_list.append(tim)

    def move(self):
        for i in self.car_list:
            new_x = i.xcor() - self.speed
            i.goto(new_x, i.ycor())

    def new_level_speed(self):
        self.speed += MOVE_INCREMENT
