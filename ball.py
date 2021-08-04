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

    def move(self, y_inc):
        self.setposition(x=self.xcor() + 5, y=self.ycor() + y_inc)

    def bounce(self):
        if self.ycor() >= 300:
            self.move(y_inc=-5)
        elif self.ycor() <= -300:
            self.move(y_inc=+5)
        else:
            pass
