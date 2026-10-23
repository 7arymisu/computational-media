from random import Random
randomColors = [ ]
randomChoice = None

def setup():
    size(400,400)
    global randomColors, randomChoice
    randomColors = [color(255, 0, 0), color(0, 255, 0), color(0, 0, 255)]
    
    randomChoice = int(random(3))

def draw():
    background(220)
    text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
    
    fill(randomColors[randomChoice])
    circle(200, 200, 100)
