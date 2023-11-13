from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball(60)
score = Scoreboard()


def hit_paddle():
    if ball.xcor() > 330 and ball.distance(paddle_right) < 50:
        ball.reflect_v()
        score.add_score_right()
        ball.move_speed *= 0.8
    if ball.xcor() < -330 and ball.distance(paddle_left) < 50:
        ball.reflect_v()
        ball.move_speed *= 0.8
        score.add_score_left()


def hit_wall():
    if ball.xcor() > 380:
        score.add_score_left()
        ball.home()
        ball.move_speed = 0.01
        ball.setheading(220)
    if ball.xcor() < -380:
        score.add_score_right()
        ball.home()
        ball.move_speed = 0.01
        ball.setheading(60)
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.reflect_h()


screen.listen()
screen.onkey(fun=paddle_left.move_up, key="w")
screen.onkey(fun=paddle_left.move_down, key="s")
screen.onkey(fun=paddle_right.move_up, key="Up")
screen.onkey(fun=paddle_right.move_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.forward(3)
    hit_wall()
    hit_paddle()







screen.exitonclick()