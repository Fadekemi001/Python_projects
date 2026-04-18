from turtle import Turtle
import random
class Ball(Turtle ):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0,0)

    def refresh(self):
        random_x = random.randint(-350, 350)
        random_y = random.randint(-350, 350)
        self.goto(random_x, random_y)