#This program uses turtle graphics to draw both a square and a triangle.
#11/3/2022
#CTI-110 P4LAB1a - Shapes
#William "James" Ross
#Pseudocode (detail algorithm)

import turtle

turtle.shape("turtle")

for i in [0,1,2,3]:
    turtle.forward(100)
    turtle.left(90)
turtle.penup()

turtle.forward(150)

turtle.pendown()
for i in [0,1,2]:
    turtle.forward(100)
    turtle.left(120)
turtle.penup()

turtle.forward(150)

turtle.exitonclick()
