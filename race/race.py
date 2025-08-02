import turtle
import random

def start_game(x ,y):
    print('Start the game')
    global num_players
    num_players = int(screen.textinput('Amount of players', 'Enter num of players(1-4): '))
    print(f'Num of players = {num_players}')


    pen.speed(0)
    pen.clear()
    pen.up()
    pen.goto(-350, -250)
    pen.down()
    pen.color('black')
    pen.pensize(3)
    for _ in range(2):
        pen.forward(700)
        pen.left(90)
        pen.forward(500)
        pen.left(90)

    start_x, start_y = -350, -200
    pen.up()
    pen.goto(start_x, start_y)
    pen.down()
    pen.color('blue')
    pen.forward(700)

    finish_x, finish_y = -350, 200
    pen.up()
    pen.goto(finish_x, finish_y)
    pen.down()
    pen.color('red')
    pen.forward(700)

    pen.up()
    pen.goto(start_x - 80, start_y - 20)
    pen.color('blue')
    pen.write('START', font=('Arial', 16, 'bold'))

    pen.up()
    pen.goto(finish_x - 80, finish_y + 20)
    pen.color('red')
    pen.write('FINISH', font=('Arial', 16, 'bold'))

    pen.hideturtle()

    obstacles = []
    for _ in range(5):
        obs = turtle.Turtle()
        obs.shape('circle')
        obs.color('black')
        obs.penup()
        obs.goto(random.randint(-300, 300),random.randint(-150, 150))
        obstacles.append(obs)

    turtles = []
    colors = ['red', 'green', 'blue', 'yellow']

    for i in range(num_players):
        t = turtle.Turtle()
        t.color(colors[i])
        t.shape('turtle')
        t.penup()
        t.goto(start_x + (700 / (num_players + 1)) * (i + 1), start_y)
        t.setheading(90)
        t.pendown()
        turtles.append(t)


    status_pen =turtle.Turtle()

    status_pen.penup()
    status_pen.hideturtle()
    status_pen.goto(0, 200)

    def update_status():
        leader = max(turtles, key= lambda t: t.ycor())
        leader_color = leader.color()[0]
        distance_to_finish = finish_y - leader.ycor()
        status_pen.clear()
        status_pen.write(f'Leader: {leader_color}. Distance to finish: {distance_to_finish}', align='center', font=('Arial', 16, 'bold'))

    race_in_progress = True
    while race_in_progress:
        for t in turtles:
            distance = random.randint(1, 10)
            t.forward(distance)

            for obs in obstacles:
                if t.distance(obs) < 20:
                    t.right(90)
                    t.forward(10)
                    t.left(90)



            if t.ycor() >= finish_y:
                race_in_progress = False
                winner = t.color()[0]
                print(f'Winner: {winner}')
                break
        update_status()


    


screen = turtle.Screen()
pen = turtle.Turtle()
screen.setup(width=1280, height=720)






pen.up()
pen.goto(-50, 0)
pen.down()

pen.color('blue')
pen.begin_fill()
for _ in range(2):
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
pen.end_fill()

pen.up()
pen.goto(0, -20)
pen.color('white')
pen.write('START', align='center', font=('Arial', 14, 'bold'))
pen.hideturtle()

screen.onscreenclick(start_game, 1)

turtle.done()