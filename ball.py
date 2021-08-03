from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)

    def random_dir(self):
        pass

    def move(self, direction):
        self.setheading(direction)
        self.forward(345)
