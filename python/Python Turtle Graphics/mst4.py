import turtle
a =turtle.getscreen()
a=turtle.Turtle()
turtle.bgcolor('black')
a.speed(100)

for i in range(200):
    a.color("green")
    a.circle(i)
    a.lt(10)

turtle.done()
