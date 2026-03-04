# import turtle
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan4 ")
# timmy.forward(100)
#
# my_screen = turtle.Screen()
# print (my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name ", ["Pikachu", "Squritle", "charmander"])
table.add_column("Type",["Eletric","water","fire"])
table.align  = "l"
print (table)