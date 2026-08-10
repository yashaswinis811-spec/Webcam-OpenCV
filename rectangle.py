import turtle

screen = turtle.Screen()
screen.title("Rectangle")

pen = turtle.Turtle()
length = 200
width = 100

for i in range(2):
    pen.forward(length)
    pen.right(90)
    pen.forward(width)
    pen.right(90)

turtle.done()