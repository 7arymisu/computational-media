from random import Random
from semester1.libraries.collide2d import *


cell = 50
shape_type = 0
palette_num = 0
grow = False
seed = 1

palettes = [
    [(197, 160, 110), (90, 184, 165), (214, 60, 190), (110, 190, 80), (60, 50, 110)],
    [(20, 50, 50), (190, 70, 50), (90, 200, 200), (30, 90, 70), (10, 10, 10)],
    [(255, 90, 120), (255, 200, 60), (80, 220, 160), (60, 120, 255), (250, 250, 250)],
]
sizes = [25, 40, 50, 80, 100]
labels = ["Size", "Shape", "Colors", "Growth", "Shuffle"]
BTN_W, BTN_H = 80, 30

def setup():
    size(800, 450)

def draw():
    no_stroke()
    rng = Random(seed)
    cols = 800 // cell + 1
    rows = 450 // cell + 1

    for row in range(rows):
        for col in range(cols):
            x = col * cell
            y = row * cell

            s = cell
            if grow:
                s = cell * (0.3 + 0.7 * col / cols)

            fill(*rng.choice(palettes[palette_num]))
            draw_shape(x, y, s, rng)

    draw_buttons()

def draw_shape(x, y, s, rng):
    if shape_type == 0:
        circle(x + cell / 2, y + cell / 2, s)
    elif shape_type == 1:
        rect(x, y, s, s)
    elif shape_type == 2:
        start = rng.choice([0, HALF_PI, PI, PI + HALF_PI])
        arc(x + cell / 2, y + cell / 2, s, s, start, start + PI)
    else:
        triangle(x, y + s, x + s, y + s, x, y)

def draw_buttons():
    text_align(CENTER, CENTER)
    text_size(14)
    for i, label in enumerate(labels):
        bx = 10 + i * (BTN_W + 10)
        by = 10
        fill(255)
        rect(bx, by, BTN_W, BTN_H)
        fill(0)
        text(label, bx + BTN_W / 2, by + BTN_H / 2)

def mouse_pressed():
    global cell, shape_type, palette_num, grow, seed
    for i, label in enumerate(labels):
        bx = 10 + i * (BTN_W + 10)
        if collidePointRect(mouse_x, mouse_y, bx, 10, BTN_W, BTN_H):
            if label == "Size":
                cell = sizes[(sizes.index(cell) + 1) % len(sizes)]
            elif label == "Shape":
                shape_type = (shape_type + 1) % 4
            elif label == "Colors":
                palette_num = (palette_num + 1) % len(palettes)
            elif label == "Growth":
                grow = not grow
            elif label == "Shuffle":
                seed += 1