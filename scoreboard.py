from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.setposition(x=-20, y=230)
        self.write(arg=f"Score {self.score_left} : {self.score_right}", move=False, align="center", font=('Arial', 40, 'normal'))

    def add_score_left(self):
        self.clear()
        self.score_left += 1
        self.write(arg=f"Score {self.score_left} : {self.score_right}", move=False, align="center", font=('Arial', 40, 'normal'))

    def add_score_right(self):
        self.clear()
        self.score_right += 1
        self.write(arg=f"Score {self.score_left} : {self.score_right}", move=False, align="center", font=('Arial', 40, 'normal'))
