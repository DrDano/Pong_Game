from turtle import Turtle, Screen
import paddle

screen = Screen()

screen.setup(height=600, width=800)
screen.title(titlestring="Pong")
screen.bgcolor("black")
screen.tracer(0)

user_paddle = paddle.Paddle()

screen.listen()
screen.onkey(fun=user_paddle.go_up(), key="Up")
screen.onkey(fun=user_paddle.go_down(), key="Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
