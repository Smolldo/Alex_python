# for i in range(2, 11, 2):
#     print(i)

# fruit = 'apple'

# for i in fruit:
#     print(i)


import turtle

t = turtle.Turtle()
wn = turtle.Screen()


# for i in range(4):
#     t.forward(100)
#     t.right(90)


# for i in range(360):
#     t.forward(1)
#     t.left(1)

# sides = 10
# length = 70

# for i in range(sides):
#     t.forward(length)
#     t.left(360 / sides)


# while True:
#     speed = input('Enter speed l, m, h. or 0 for exit: ')
#     if speed == 'l':
#         t.speed(1)
#     elif speed == 'm':
#         t.speed(5)
#     elif speed == 'h':
#         t.speed(10)
#     elif speed == '0':
#         break
#     else:
#         print('unknown command')

#     t.forward(100)
#     t.right(85)

import colorsys

def draw_spiral():
    t.speed(0)
    wn.bgcolor('black')
    n = 36
    for i in range(360):
        color = colorsys.hsv_to_rgb(i/n, 1, 1)
        t.pencolor(color)
        t.forward(i * 3 / n + i)
        t.right(59)

draw_spiral()
turtle.done()