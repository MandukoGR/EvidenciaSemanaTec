"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import color, up, goto, down, circle, update
from turtle import setup, hideturtle, tracer, onscreenclick, done
from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color("red")
    line(x+60, y+60, x + 66.5, y + 66.5)
    line(x+60, y + 66.5, x + 66.5, y+60)


def drawo(x, y):
    """Draw O player."""
    color("green")
    up()
    goto(x + 67, y + 40)
    down()
    circle(31)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
"""Number for each position and value (1 taken 0 empty)"""
positions = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    square = [x, y]  # Coordinates of square
    pos = 0
    """Conditions for getting square position"""
    if square == [-200, 66]:
        pos = 1
    elif square == [-67, 66]:
        pos = 2
    elif square == [66, 66]:
        pos = 3
    elif square == [-200, -67]:
        pos = 4
    elif square == [-67, -67]:
        pos = 5
    elif square == [66, -67]:
        pos = 6
    elif square == [-200, -200]:
        pos = 7
    elif square == [-67, -200]:
        pos = 8
    elif square == [66, -200]:
        pos = 9
    """Validation for checking if the spot is taken"""
    if(positions[pos] == 0):
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        positions[pos] = 1


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
