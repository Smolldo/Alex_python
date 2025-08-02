age = 98

if age < 18:
    print('u r under 18')
elif age >= 18 and age < 65:
    print('u r adult')
else:
    print('u r pensioner')


answer = 'asdasdasda'


if answer == 'YES':
    print('answer is YES')
elif answer == 'NO':
    print('answer is NO')
else:
    print('unknown answer')


import turtle

t = turtle.Turtle()
screen = turtle.Screen()

# direction = input('Enter direction (up, down, lef, right): ')

# if direction == 'up':
#     t.left(90)
#     t.forward(100)
# elif direction == 'down':
#     t.right(90)
#     t.forward(100)
# elif direction == 'right':
#     t.forward(100)
# elif direction == 'left':
#     t.right(180)
#     t.forward(100)
# else:
#     print('wrong direction')


distance = int(input('Enter distance: '))

if distance < 50:
    t.speed(1)
elif distance >= 50 and distance < 100:
    t.speed(5)
else:
    t.speed(10)

t.forward(distance)

turtle.done()