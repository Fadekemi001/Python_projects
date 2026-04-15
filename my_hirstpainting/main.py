# import colorgram
# colors = colorgram.extract('image.jpeg', 30)
#
# rgb_colors = []
# for color in colors:
#
#     rgb = color.rgb
#     #r, g, b = rgb.r, rgb.g, rgb.b
#     rgb_colors.append((rgb.r, rgb.g, rgb.b))
# print(rgb_colors)
import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")
tim.penup()

# 🎨 Your colors
color_list = [
    (249, 229, 236), (240, 250, 244), (29, 41, 60), (49, 92, 143),
    (145, 81, 44), (170, 14, 28), (160, 56, 87), (227, 154, 8)
]

# 📦 Draw square background
square_size = 300

tim.goto(-150, -150)  # bottom-left corner

for _ in range(4):
    tim.forward(square_size)
    tim.left(90)


# 🎯 Move inside square to start dots
start_x = -130
start_y = -130

tim.goto(start_x, start_y)

# 🔵 Draw grid of dots inside square
rows = 10
cols = 10
spacing = 50

for row in range(rows):
    for col in range(cols):
        tim.dot(15, random.choice(color_list))
        tim.forward(spacing)
    tim.backward(spacing * cols)
    tim.left(90)
    tim.forward(spacing)
    tim.right(90)

screen = t.Screen()
screen.exitonclick()