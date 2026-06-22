from turtle import *

t = Turtle()
t.speed(5)
t.pensize(5)

rings = [
    ("blue", -120, 0),
    ("black", 0, 0),
    ("red", 120, 0),
    ("yellow", -60, -50),
    ("green", 60, -50)
]

for color, x, y in rings:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    t.circle(50)

hideturtle()
mainloop()