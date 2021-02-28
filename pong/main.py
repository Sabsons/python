from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


#Create screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#Create Paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

#Screen properties
screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down,"s")

x = 10
y = 10


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move(x,y)

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    elif  ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()

