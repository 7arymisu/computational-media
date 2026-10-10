from semester1.libraries.collide2d import *

def setup():
    size(300,600)

def draw():
    color_mode(HSB,360,100,100)
    background(220)
    fill(0,25,100)
    circle(150, 75, 150)
    fill(60,25,100)
    circle(150, 300, 150)
    fill(120,25,100)
    circle(150, 525, 150)

#BUG: The collidePointCircle function is not working properly. It is not detecting when the mouse is inside the circle. I will need to debug this function and see what is going wrong.
# def mouse_pressed():
#     if collidePointCircle(mouse_x, mouse_y, 150, 75, 150):
#         fill(0,100,100)
#     elif collidePointCircle(mouse_x, mouse_y, 150, 300, 150):
#         fill(60,100,100)
#     elif collidePointCircle(mouse_x, mouse_y, 150, 525, 150):
#         fill(120,100,100)