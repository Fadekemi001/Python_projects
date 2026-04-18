from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle


screen = Screen()
paddle = Turtle()

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

while is_game_on:
    screen.update()
    ball.refresh()



screen.exitonclick()