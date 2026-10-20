from semester1.libraries.collide2d import *

#SETTINGS
TOOLBAR_H = 85 # height of the toolbar at the top
SQ = 30 # size of each palette square
GAP = 35 # space between palette squares

#DICTIONARIES
brush = {
    "color": (0, 0, 0),
    "size": 10,
    "shape": "circle",
    "eraser": False
}

palette = {
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "yellow": (255, 255, 0),
    "green": (0, 200, 0),
    "blue": (0, 0, 255),
    "purple": (150, 0, 200),
    "brown": (120, 70, 20),
    "black": (0, 0, 0)
}

buttons = {
    "Clear": 10,
    "Eraser": 90,
    "Random": 170,
    "Shape": 250
}

BTN_Y = 45
BTN_W = 70
BTN_H = 30


def setup():
    size(600, 500)
    background(255)


def draw():
    draw_toolbar()
    if is_mouse_pressed and mouse_y > TOOLBAR_H and pmouse_y > TOOLBAR_H:
        draw_stroke()

#DRAW TOOLS
def get_draw_color():
    if brush["eraser"]:
        return (255, 255, 255)
    return brush["color"]


def draw_stroke():
    c = get_draw_color()
    s = brush["size"]
    if brush["shape"] == "circle":
        no_stroke()
        fill(c[0], c[1], c[2])
        circle(mouse_x, mouse_y, s)
    elif brush["shape"] == "square":
        no_stroke()
        fill(c[0], c[1], c[2])
        square(mouse_x - s / 2, mouse_y - s / 2, s)
    elif brush["shape"] == "line":
        stroke(c[0], c[1], c[2])
        stroke_weight(s)
        line(pmouse_x, pmouse_y, mouse_x, mouse_y)


def draw_toolbar():
    stroke(0)
    stroke_weight(1)
    fill(220)
    rect(0, 0, width, TOOLBAR_H)

    # palette squares
    i = 0
    for name in palette:
        c = palette[name]
        fill(c[0], c[1], c[2])
        square(10 + i * GAP, 5, SQ)
        i += 1

    # buttons
    for label in buttons:
        fill(255)
        rect(buttons[label], BTN_Y, BTN_W, BTN_H)
        fill(0)
        text_size(14)
        text(label, buttons[label] + 8, BTN_Y + 20)

    c = get_draw_color()
    fill(c[0], c[1], c[2])
    square(510, 5, 40)
    fill(0)
    text_size(12)
    text(brush["shape"] + " / size " + str(brush["size"]), 340, 65)
    if brush["eraser"]:
        text("ERASER ON", 340, 50)


def clear_canvas():
    no_stroke()
    fill(255)
    rect(0, TOOLBAR_H, width, height - TOOLBAR_H)


def random_color():
    brush["color"] = (int(random(256)), int(random(256)), int(random(256)))
    brush["eraser"] = False


def next_shape():
    if brush["shape"] == "circle":
        brush["shape"] = "square"
    elif brush["shape"] == "square":
        brush["shape"] = "line"
    else:
        brush["shape"] = "circle"


def toggle_eraser():
    brush["eraser"] = not brush["eraser"]


def change_size(amount):
    brush["size"] = brush["size"] + amount
    if brush["size"] < 2:
        brush["size"] = 2
    if brush["size"] > 60:
        brush["size"] = 60


def mouse_pressed():
    i = 0
    for name in palette:
        if collidePointRect(mouse_x, mouse_y, 10 + i * GAP, 5, SQ, SQ):
            brush["color"] = palette[name]
            brush["eraser"] = False
        i += 1

    # buttons
    for label in buttons:
        if collidePointRect(mouse_x, mouse_y, buttons[label], BTN_Y, BTN_W, BTN_H):
            if label == "Clear":
                clear_canvas()
            elif label == "Eraser":
                toggle_eraser()
            elif label == "Random":
                random_color()
            elif label == "Shape":
                next_shape()

#KEYS
def key_pressed():
    if key == "c":
        clear_canvas()
    elif key == "e":
        toggle_eraser()
    elif key == "r":
        random_color()
    elif key == "s":
        next_shape()
    elif key == "=" or key == "+":
        change_size(5)
    elif key == "-":
        change_size(-5)