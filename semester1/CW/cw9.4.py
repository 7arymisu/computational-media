def setup():
    size(480, 480)

def draw():
    background(180)
    fill(255)

    for i in range(40, height, 40):
        for j in range(40, width, 40):
            circle(j, i, 20)