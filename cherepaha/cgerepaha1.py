import turtle

t = turtle.Turtle()

wn = turtle.Screen()

wn.title('My first game')
wn.bgcolor('lightblue')

wn.setup(width=600, height=600)


#turtle

# t.forward(150)

# t.left(90)
# t.forward(150)
# t.left(120)
# t.forward(200)
# t.backward(260)


# up() penup()
# t.up()
# t.forward(200)

# down() pendown()
# t.pendown()
# t.forward(100)

#reset()
# t.reset()

#clear()
# t.clear()

#goto()
# t.goto(250, 420)

# t.circle(50)

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.left(45)
t.forward(50)

t.up()
t.goto(100,0)
t.down()
t.forward(50)

t.up()
t.goto(100, 100)
t.down()
t.forward(50)

t.up()
t.goto(0, 100)
t.down()
t.forward(50)

t.right(45)
t.up()
t.goto(35,35)
t.down()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

wn.mainloop()


