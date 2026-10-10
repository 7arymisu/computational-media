# def setup():
#     size(400,400)

#     arc(50, 55, 50, 50, 0, HALF_PI)
#     no_fill()
#     arc(50, 55, 60, 60, HALF_PI, PI)
#     arc(50, 55, 70, 70, PI, PI + QUARTER_PI)
#     arc(50, 55, 80, 80, PI + QUARTER_PI, TWO_PI)

#     fill(255)
#     arc(50, 150, 80, 80, 0, PI + QUARTER_PI, OPEN)
#     arc(50, 250, 80, 80, 0, PI + QUARTER_PI, CHORD)
#     arc(50, 350, 80, 80, 0, PI + QUARTER_PI, PIE)

def setup():
    size(400,400)
    
def draw():
    triangle(50,25,125,50,75,75)
    quad(275,50,350,75,300,125,250,75)
    begin_shape()
    vertex(175,100)
    vertex(225,125)
    vertex(225,175)
    vertex(175,200)
    vertex(125,175)
    vertex(175,150)
    vertex(150,125)
    end_shape(CLOSE) # connects the last vertex to the first