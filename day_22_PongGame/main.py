from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

# control the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("gray10")
screen.title("Pong Game")
# turn off the animation.
screen.tracer(0)

# two paddle objects.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = ScoreBoard()

# control paddles movements.
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# turn off paddle animation.
game_on = True
while game_on:
    screen.update()
    ball.move()

    # detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when r_paddle misses.
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # detect when l_paddle misses.
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
