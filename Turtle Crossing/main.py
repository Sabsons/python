import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.createCar()
    car.move()

    # If turtle reaches top
    if player.winCondition():
        player.return_home()
        car.new_level_speed()
        scoreboard.new_level_score()

    # Detect Collision with cars:
    for i in range(len(car.car_list)):
        if player.distance(car.car_list[i]) < 25:
            scoreboard.game_over()
            game_is_on = False






screen.exitonclick()