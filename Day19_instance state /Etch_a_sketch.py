from turtle import Turtle , Screen
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_drawing ():
    tim.reset()


screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="C", fun=clear_drawing)


screen.exitonclick()
