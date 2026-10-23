def setup():
    size(400,400)

    arc(50, 55, 50, 50, 0, HALF_PI)
    
    no_fill()
    arc(50, 55, 60, 60, HALF_PI, PI)
    arc(50, 55, 70, 70, PI, PI + QUARTER_PI)
    arc(50, 55, 80, 80, PI + QUARTER_PI, TWO_PI)

    fill(255)
    arc(50, 150, 80, 80, 0, PI + QUARTER_PI, OPEN)
    arc(50, 250, 80, 80, 0, PI + QUARTER_PI, CHORD)
    arc(50, 350, 80, 80, 0, PI + QUARTER_PI, PIE)