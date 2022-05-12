from random import randint, shuffle
from turtle import up, goto, down, color, begin_fill, forward
from turtle import left, end_fill, clear, shape, stamp, write
from turtle import update, ontimer, setup, addshape, hideturtle
from turtle import tracer, onscreenclick, done
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

# Counter for taps.
global taps
taps = 0

# Counter to keep score of how many tiles have been uncovered
global points
points = 0


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps, points

	# Get the index of the selected tile
    spot = index(x, y)
    
    # Obtain the last tile
    mark = state['mark']

	# Increment the number of taps
    taps += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        
        # Indicate that two tiles have been uncovered
        points += 2


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

	# Draw a square for each hidden tile
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

	# Draw the number of the tile on the last selected tile
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

	# Draw the number of taps
    goto(50, 200)
    color('black')
    write('Taps: ' + str(taps), font=('Arial', 30, 'normal'))

	#If all tiles have been uncovered, announce success
    if(points == 64):
        goto(-200, 200)
        
        #Use a random color
        color(randint(0, 100)/100.0,
              randint(0, 100)/100.0,
              randint(0, 100)/100.0)
        
        write("Success!", font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 520, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
