from turtle import Turtle


class Ball(Turtle):
    def __init__(self, heading_angle):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(heading_angle)
        self.penup()
        self.move_speed = 0.01

    def reflect_v(self):
        self.setheading(180 - self.heading())

    def reflect_h(self):
        self.setheading(360 - self.heading())

