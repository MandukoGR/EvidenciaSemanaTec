from random import choice
import turtle
from freegames import floor, vector

state = {'score': 0}
path = turtle.Turtle(visible=False)
writer = turtle.Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)
# The second vector of the array defines how fast the ghosts
# move in the first movement
ghosts = [
    [vector(-180, 160), vector(15, 0)],
    [vector(-180, -160), vector(0, 15)],
    [vector(100, 160), vector(0, -15)],
    [vector(100, -160), vector(-15, 0)],
]
# Defines in which tiles of the board
# can the ghosts and pacman move. (The ones that have the value 1)
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]


def square(x, y):
    # Draw square using path at (x, y).
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    # Return offset of point in tiles.
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    # Return True if point is valid in tiles.
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    # Draw world using path.
    # The method bgcolor will change the background color of the board
    turtle.bgcolor('black')
    # The method color will change the color of the tiles that can be passed by
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                # The next line of code will define the color
                # of the "fruits" that pacman needs to eat
                path.dot(4, 'yellow')
            if tile == 2:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(10, 'red')


def move():
    # Move pacman and all ghosts.
    writer.undo()
    writer.write(state['score'])

    turtle.clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 3
        state['score'] += 10
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)
    elif tiles[index] == 2:
        tiles[index] = 3
        state['score'] += 100
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    turtle.up()
    turtle.goto(pacman.x + 10, pacman.y + 10)
    # The next line of code will define the color of pacman and its size
    turtle.dot(20, 'yellow')
    counterGhost = 1
    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            # The array "options" defines the ghosts speed
            options = [
                vector(15, 0),
                vector(-15, 0),
                vector(0, 15),
                vector(0, -15),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        turtle.up()
        turtle.goto(point.x + 10, point.y + 10)
        # The next line of code will define the color of the ghosts
        if counterGhost == 1:
            turtle.dot(20, 'red')
            counterGhost = counterGhost + 1
        elif counterGhost == 2:
            turtle.dot(20, 'pink')
            counterGhost = counterGhost + 1
        elif counterGhost == 3:
            turtle.dot(20, 'orange')
            counterGhost = counterGhost + 1
        elif counterGhost == 4:
            turtle.dot(20, 'cyan')
    turtle.update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    turtle.ontimer(move, 100)


def change(x, y):
    # Change pacman aim if valid.
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


# The setup method sets the window size of the game
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
# The listen method will receive the user's input
turtle.listen()
# The next four lines of code defines the movement
# of pacman according to the input
turtle.onkey(lambda: change(5, 0), 'Right')
turtle.onkey(lambda: change(-5, 0), 'Left')
turtle.onkey(lambda: change(0, 5), 'Up')
turtle.onkey(lambda: change(0, -5), 'Down')
# The method world initializes the board
world()
move()
turtle.done()
