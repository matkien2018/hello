import turtle
""" https://docs.python.org/3/library/turtle.html#turtle.pen """
w = turtle.Screen()
w.bgcolor("lightgreen")
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

t.penup()
size = 20
for i in range(30):
    t.stamp()
    size = size + 3
    t.forward(size)
    t.right(24)
#t.pen(pencolor="purple", fillcolor="#99cfe0", pensize=10, speed=2)
w.mainloop()
