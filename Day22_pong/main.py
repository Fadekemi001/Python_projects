from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time



screen = Screen()
tim = Turtle()

screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.listen()

is_game_on = True

# paddle.shape("square")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.color("white")
# paddle.penup()
#
#
# paddle.setposition(350, 0)
paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))

screen.onkey(paddle_1.paddle_up, "Up")
screen.onkey(paddle_1.paddle_down, "Down")

screen.onkey(paddle_2.paddle_up, "w")
screen.onkey(paddle_2.paddle_down, "s")

ball = Ball()
scoreboard = Scoreboard()



while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting collusion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detecting collusion with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #detect ball past the  paddle
    if ball.xcor() > 370 :
        ball.reset_position()
        scoreboard.l_point()
        # is_game_on = False
        # tim.color("red")
        # tim.write("GAME OVER", align="center", font="Arial")
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()