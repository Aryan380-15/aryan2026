from turtle import *

t = Turtle()
t.speed(6)
t.pensize(1)

colors = ["red", "blue", "green", "orange", "purple"]
def star():
    for i in range(50):
        t.pencolor(colors[i%5])
        t.forward(i*15)
        t.right(144)
star()

hideturtle()
mainloop()