from semester1.libraries.collide2d import *

memes = [
    'semester1/images/meme-1.jpeg',
    'semester1/images/meme-2.jpeg',
    'semester1/images/meme-3.jpeg',
    'semester1/images/meme-4.jpeg',
    'semester1/images/meme-5.jpeg'
]

images = []
meme = {}

BTN_X, BTN_Y, BTN_W, BTN_H = 120, 350, 160, 40

def setup():
    size(400, 400)
    for path in memes:
        images.append(load_image(path))
    reroll()

def pick(items):
    return items[int(random(0, len(items)))]

def reroll():
    global meme
    meme = {
        "image": pick(images)
    }

def draw():
    background(0)
    image(meme["image"], 0, 0, width, height)

    fill(255)
    rect(BTN_X, BTN_Y, BTN_W, BTN_H)
    fill(0)
    text_size(18)
    text_align(CENTER, CENTER)
    text("Reroll", BTN_X + BTN_W / 2, BTN_Y + BTN_H / 2)

def mouse_pressed():
    if collidePointRect(mouse_x, mouse_y, BTN_X, BTN_Y, BTN_W, BTN_H):
        reroll()