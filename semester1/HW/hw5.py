from semester1.libraries.collide2d import *

circle1_clicked = False
circle2_clicked = False
circle3_clicked = False

def setup():
    size(300, 600)

def draw():
    color_mode(HSB, 360, 100, 100)
    background(0, 0, 86)

    if circle1_clicked:
        fill(0, 100, 100)
    else:
        fill(0, 25, 80)
    circle(150, 75, 150)

    if circle2_clicked:
        fill(60, 100, 100)
    else:
        fill(60, 25, 80)
    circle(150, 300, 150)

    if circle3_clicked:
        fill(120, 100, 100)
    else:
        fill(120, 25, 80)
    circle(150, 525, 150)

def mouse_pressed():
    global circle1_clicked, circle2_clicked, circle3_clicked
    if collidePointCircle(mouse_x, mouse_y, 150, 75, 150):
        circle1_clicked = True
    elif collidePointCircle(mouse_x, mouse_y, 150, 300, 150):
        circle2_clicked = True
    elif collidePointCircle(mouse_x, mouse_y, 150, 525, 150):
        circle3_clicked = True