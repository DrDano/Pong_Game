from turtle import Turtle
POSITION = (350, 0)

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=20, stretch_len=100)
        self.setposition(POSITION)
