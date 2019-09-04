import turtle

wn = turtle.Screen()
wn.bgcolor("black")

baby = turtle.Turtle()
baby.color("aquamarine4")
baby.pensize(30)
baby.speed(0)

baby.penup()
baby.backward(250)
baby.right(90)
baby.forward(100)
baby.right(180)
baby.pendown()
baby.forward(190)


for first_curve in range(60):
    baby.forward(3)
    baby.right(3)

baby.forward(80)
baby.right(180)
baby.forward(80)

for second_curve in range(60):
    baby.forward(3)
    baby.right(3)

baby. forward(190)
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

wn.exitonclick()