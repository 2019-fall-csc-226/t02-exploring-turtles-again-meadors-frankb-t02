#######################################################################
# Set up Turtle
import turtle
wn = turtle.Screen()
wn.bgcolor("black")

#######################################################################
# Define a new turtle object named baby
baby = turtle.Turtle()
baby.color("aquamarine4")
baby.pensize(30)
baby.speed(0)

# navigate baby toward initial drawing point
baby.penup()
baby.backward(250)
baby.right(90)
baby.forward(100)
baby.right(180)
baby.pendown()
########################################################################
# first leg of M
baby.forward(190)
# make the first curve for M
for first_curve in range(60):
    baby.forward(3)
    baby.right(3)
# middle leg of M
baby.forward(80)
baby.right(180)
baby.forward(80)
# second curve for M
for second_curve in range(60):
    baby.forward(3)
    baby.right(3)
# last leg for M
baby. forward(190)
#########################################################################
# set up turtle and draw F
baby.left(90)
baby.penup()
baby.forward(100)
baby.pendown()
baby.pencolor("lightgreen")
baby.left(90)
baby.forward(140)
baby.right(90)
baby.forward(90)
baby.backward(90)
baby.left(90)
baby.forward(100)
baby.right(90)
baby.forward(140)
##########################################################################
wn.exitonclick()