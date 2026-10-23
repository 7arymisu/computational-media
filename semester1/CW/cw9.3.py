def setup():
    size(600, 125)

def draw():
    background(180)
    fill(255)
    color_mode(HSB, 360, 100, 100)

    for i in range(1, 6):
        fill(240, 100, i * 15)
        circle(i * 100, 62, 50)