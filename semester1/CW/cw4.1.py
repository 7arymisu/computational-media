# ================================
# Using Random to randomize size:
# ================================

circW = None
def setup():
    size(400,400)
    global circW
    circW = random(50, 150)
def draw():
    background(220)
    ellipse(200, 200, circW, 100)