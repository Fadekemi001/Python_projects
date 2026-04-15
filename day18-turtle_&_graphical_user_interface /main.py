import random
import turtle as t
import  random

tim = t.Turtle()



tim.shape("arrow")

tim.color("green", "yellow")
tim.speed(1)

# This to draw a square
# for i in range (4):
#     tim .forward(100)
#     tim.left(90)# THE 90 stands for degrees direction uses dergees
# tim.home()


# #This is to draw a dashed line
# for i in range (15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# This is to draw different shapes
# i = 3
# d =['blue', 'red', 'green']
# while i > 2 :
#     degree = 360 / i
#     c = random.choice(d)
#     for _ in range (i):
#         tim.color(c)
#         tim .forward(100)
#         tim.left(degree)
#



#Ths is to draw a random
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

direction = [0,90,180,270]
colors = ["khaki1","brown1", "DeepPink", "medium blue","dark green", "red", "magenta", "midnight blue"]
fo = [20,30,40,35,25]
tim.speed("fastest")
def walk (t):
    for _ in range(t):
        tim.color(random_color())
        tim.seth(random.choice(direction))
        tim.pensize(10)
        tim.forward(random.choice(fo))



for i in range(1,100):
    # tim.seth(random.choice(direction))
    #tim.color(random.choice(colors))-> the mistake was i put it here
    walk(i)








screen = Screen()# makes the window stay and not disappear till the window is clicked on
screen.exitonclick()