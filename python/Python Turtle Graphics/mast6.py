import turtle
color =['red','purple','blue','green','orange','yellow']
t =turtle.Pen()
turtle.bgcolor('black')

for i in range(360):
    t.pencolor(color[i%6])
    t.width(i//100 +1)
    t.fd(i)
    t.lt(59)

turtle.done()