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
ball = Ball()

screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")

# All autonomous movement code
game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.05)
    ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # Detect ball going out of bounds
    ball.ball_reset()

screen.exitonclick()
