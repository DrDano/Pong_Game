from turtle import Turtle
POSITION = (350, 0)

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=10)
        self.penup()
        self.right(90)
        self.setposition(POSITION)
        self.showturtle()
