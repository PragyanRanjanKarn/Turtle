import turtle

# Background color
turtle.bgcolor("sky blue")

# Set up the turtle
t = turtle.Turtle()
t.speed(3)

# Draw an equilateral triangle
t.color("red")
for i in range(3):
    t.forward(100) 
    t.left(120) 

# Draw a square
t.color("green")
for i in range(4):
    t.forward(100)
    t.left(90)    

# Draw a rectangle
t.color("blue")
for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)

# Draw a pentagon
t.color("purple")
for i in range(5):
    t.forward(100)
    t.left(72)

# Draw a hexagon
t.color("orange")
for i in range(6):
    t.forward(100)
    t.left(60)

# Draw an octagon
t.color("brown")
for i in range(8):
    t.forward(100)
    t.left(45)

# Draw a star
t.color("black")
for i in range(5):
    t.forward(100)
    t.right(144)


