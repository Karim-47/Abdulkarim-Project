import turtle

page = turtle.Screen()
page.bgcolor("purple")
page.setup(500,500)
page.title("SQUARE")

angle = 90
length= 100

pen = turtle.Turtle()
pen.penup()
pen.left(angle)
pen.forward(50)
pen.left(angle)
pen.backward(30)
pen.pendown()

for i in range(4):
    pen.forward(length)
    pen.right(angle)


turtle.done()
