from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.setup(height=600, width=800)
screen.title(titlestring="Pong")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")

ball1 = Ball()
time.sleep(0.1)
ball1.move(45)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
