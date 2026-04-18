from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()

snake= Snake()
food =Food()

screen.listen()

screen.onkey(snake.down,"Down")
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #def collusion with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #def collusion with wall
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390 :
        game_is_on = False
        scoreboard.game_over()


    #def collusion with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
# tim.shapesize(stretch_wid=1, stretch_len=3)
# tim.penup()
#
# is_game_on = True
#
# def move():
#     global is_game_on
#     if is_game_on:
#         tim.forward(1)
#
#         # boundary check
#         if tim.xcor() > 380 or tim.xcor() < -380 or tim.ycor() > 280 or tim.ycor() < -280:
#             is_game_on = False
#
#         screen.ontimer(move, 20)
#
# def up():
#     tim.setheading(90)
#
# def right():
#     tim.setheading(0)
#
# def left():
#     tim.setheading(180)
#
# def down():
#     tim.setheading(270)
#
# screen.listen()
# screen.onkey(up, "a")
# screen.onkey(right, "r")
# screen.onkey(left, "l")
# screen.onkey(down, "d")
#
# move()
#
