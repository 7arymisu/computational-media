# =================================
# Using Random to randomize color: 
# =================================

cor = color(random(255),random(255),random(255))

# Note: RGB has a 4th argument: Alpha (transparency)
def setup():
    size(400,400)
    
def draw():
    background(220)
    fill(cor)
    ellipse(200, 200, 100, 100)