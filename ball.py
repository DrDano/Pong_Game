import random
import time
from turtle import Turtle
from random import choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 7
        self.y_move = 7

    def random_dir(self):
        pass

    def move(self):
        self.setposition(x=self.xcor() + self.x_move, y=self.ycor() + self.y_move)

    def bounce_y(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.y_move *= -1
        else:
            pass

    def bounce_x(self):
        self.x_move *= -1

    def r_ball_reset(self):
        if self.xcor() > 381:
            self.home()
            time.sleep(1)
            self.bounce_x()

    def l_ball_reset(self):
        if self.xcor() > -381:
            self.home()
            time.sleep(1)
            self.bounce_x()



