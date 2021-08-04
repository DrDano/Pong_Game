from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.setup(height=600, width=800)
screen.title(titlestring="Pong")
screen.bgcolor("black")
screen.tracer(0)

# All initializers
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball1 = Ball()

screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")

# All autonomous movement code
game_is_on = True
while game_is_on:
    ball1.move()
    screen.update()
    time.sleep(0.05)
    ball1.bounce()

screen.exitonclick()
