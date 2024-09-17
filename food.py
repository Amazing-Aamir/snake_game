from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('slowest')
        self.penup()
        self.shape('circle')
        self.shapesize(0.5)
        self.color('dark red')

    def location(self):
        x = random.randint(-280,280)
        y = random.randint(-280,250)
        self.goto(x,y)
