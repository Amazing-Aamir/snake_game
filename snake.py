from turtle import Turtle

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')

    def body_color(self):
        self.color('green')

    def move_forward(self,segment):
        for seg in range(len(segment) - 1, 0, -1):
            x = segment[seg -1].xcor()
            y = segment[seg -1].ycor()
            segment[seg].goto(x,y)
        self.forward(20)

    def move_up(self):
        if self.heading() != 270:
            self.setheading(90)

    def move_down(self):
        if self.heading() != 90:
            self.setheading(270)

    def move_left(self):
        if self.heading() != 0:
            self.setheading(180)

    def move_right(self):
        if self.heading() != 180:
            self.setheading(0)
