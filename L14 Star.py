import turtle

paper = turtle.Screen()
paper.title("STAR")
pen = turtle.Turtle()

angle = 360 / 3 

for i in range(3):
    pen.forward(100)
    pen.left(angle)

pen.penup()
pen.right(30)
pen.forward(57.5)

pen.pendown()
pen.left(90)
for i in range(3):
    pen.forward(100)
    pen.left(angle)

turtle.done()

