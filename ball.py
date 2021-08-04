from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10

    def random_dir(self):
        pass

    def move(self):
        self.setposition(x=self.xcor() + self.x_move, y=self.ycor() + self.y_move)

    def bounce(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.y_move *= -1
        else:
            pass
