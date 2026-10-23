from random import Random
stars = []
num_stars = 200

def setup():
    size(400,400)
    frame_rate(10)
    color_mode(HSB, 360, 100, 100, 1)
    global stars
    for _ in range(num_stars):
        stars.append({'color': color(random(0, 50), 0, random(100)), 'x': int(random(1, width)), 'y': int(random(1, height))})
def draw():
    background(0)
    for star in stars:
        fill(star['color'])
        circle(star['x'], star['y'], int(random(1, 8)))