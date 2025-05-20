import turtle
turtle.speed(0)
turtle.bgcolor("black")

for i in range(5):
    for colours in ["red", "red", "red", "purple", "blue", "purple"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.lt(12)
        for i in range(4):
            turtle.fd(200)
            turtle.lt(90)
