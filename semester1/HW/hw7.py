from semester1.libraries.collide2d import *

def setup():
    size(400, 400)

def draw():
    background(220)

    # everything starts white each frame
    white = (255, 255, 255)
    c1 = c2 = c3 = c4 = c5 = c6 = white

    # hover rules only set colors, nothing is drawn here
    if collidePointCircle(mouse_x, mouse_y, 100, 150, 100):  # circle 1
        c1 = (173, 216, 230)  # light blue

    if collidePointCircle(mouse_x, mouse_y, 200, 150, 100):  # circle 2
        c4 = (128, 0, 128)  # purple
        c6 = (128, 0, 128)

    if collidePointCircle(mouse_x, mouse_y, 300, 150, 100):  # circle 3
        c3 = (0, 0, 0)  # black
        c5 = (0, 0, 0)

    if collidePointCircle(mouse_x, mouse_y, 100, 250, 100):  # circle 4
        c1 = (255, 0, 0)  # red top row
        c2 = (255, 0, 0)
        c3 = (255, 0, 0)

    if collidePointCircle(mouse_x, mouse_y, 200, 250, 100):  # circle 5
        c1 = (0, 255, 0)  # green

    if collidePointCircle(mouse_x, mouse_y, 300, 250, 100):  # circle 6
        c4 = (255, 165, 0)  # orange

    # draw each circle exactly once
    fill(*c1)
    circle(100, 150, 100)
    fill(*c2)
    circle(200, 150, 100)
    fill(*c3)
    circle(300, 150, 100)
    fill(*c4)
    circle(100, 250, 100)
    fill(*c5)
    circle(200, 250, 100)
    fill(*c6)
    circle(300, 250, 100)