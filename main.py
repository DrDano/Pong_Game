from turtle import Turtle, Screen
import paddle

screen = Screen()

screen.setup(height=600, width=800)
screen.title(titlestring="Pong")
screen.bgcolor("black")

paddle.Paddle()

screen.exitonclick()
