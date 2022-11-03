#This program uses turtle graphics to draw my first and last initials.
#11/3/2022
#CTI-110 P4LAB1b - Initials
#William "James" Ross
#Pseudocode (detail algorithm)

import turtle

turtle.shape("turtle")

turtle.penup()
turtle.backward(200)
turtle.pendown()
turtle.pensize(10)
turtle.color("blue")

turtle.right(65)
turtle.forward(100)
turtle.left(130)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.left(130)
turtle.forward(100)

turtle.penup()
turtle.right(75)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(180)

turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.right(75)
turtle.forward(50)
turtle.penup()
turtle.forward(100)

turtle.exitonclick()
