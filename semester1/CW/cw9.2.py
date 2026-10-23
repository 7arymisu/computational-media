def setup():
    size(600, 125)

def draw():
    background(180)
    fill(255)

    for i in range(1, 6):
        circle(i * 100, 62, i * 10)