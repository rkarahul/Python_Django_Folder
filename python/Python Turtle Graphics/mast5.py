import turtle
star=turtle.Turtle()

for i in range(5):
    star.rt(144)
    star.fd(100)

star.begin_fill()
star.fillcolor('red')
star.end_fill()

turtle.done()