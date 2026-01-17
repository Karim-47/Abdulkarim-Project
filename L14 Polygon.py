import turtle as t

sides = int(input("Enter the number of sides of the polygon: "))
length = int(input("Enter the length of each side: "))
angle = 360/sides

paper= t.Screen()
paper.bgcolor("green")
paper.setup(500,500)
paper.title("Polygon")

pen = t.Turtle()
pen.right(angle)

for i in range(sides):
    pen.forward(length)
    pen.left(angle)

t.done()