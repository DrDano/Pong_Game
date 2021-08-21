from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")

# All autonomous movement code
game_is_on = True
game_speed = 0.05
while game_is_on:
    scoreboard.update_scoreboard()
    ball.move()
    screen.update()
    time.sleep(game_speed)
    ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # Detect ball going out of bounds
    if ball.xcor() > 381:
        scoreboard.l_point()
        game_speed *= 0.9
        ball.ball_reset()

    if ball.xcor() < -385:
        scoreboard.r_point()
        game_speed *= 0.9
        ball.ball_reset()

screen.exitonclick()
