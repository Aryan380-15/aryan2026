from turtle import *

t = Turtle()
t.speed(5)


def rectangle(length, width, color):
    t.fillcolor(color)
    t.begin_fill()

    for _ in range(2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)

    t.end_fill()


def chakra(radius):
    t.pencolor("blue")

    # Outer circle
    t.circle(radius)

    # 24 spokes
    t.penup()
    t.left(90)
    t.forward(radius)
    t.pendown()

    for _ in range(24):
        t.forward(radius)
        t.backward(radius)
        t.left(15)


# Pole
t.penup()
t.goto(-200, 250)
t.pendown()

t.right(90)
t.forward(500)

# Saffron Strip
t.penup()
t.goto(-192, 0)
t.setheading(0)
t.pendown()

rectangle(250, 60, "orange")

# White Strip (Chakra ke liye)
t.penup()
t.goto(-192, -60)
t.setheading(0)
t.pendown()

for _ in range(2):
    t.forward(250)
    t.right(90)
    t.forward(60)
    t.right(90)

# Green Strip
t.penup()
t.goto(-192, -120)
t.setheading(0)
t.pendown()

rectangle(250, 60, "green")

# Ashok Chakra
t.penup()
t.goto(-67, -90)
t.setheading(0)
t.pendown()

chakra(30)

hideturtle()
mainloop()