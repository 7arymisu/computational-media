def setup(): 
    size(400,400)

def draw(): 
    background(220)

    #Top left
    square(0,0,50)
    circle(25,25,50)

    #Top right
    square(350,0,50)
    circle(375,25,50)

    #Bottom left
    square(0,350,50)
    circle(25,375,50)

    #Bottom right
    square(350,350,50)
    circle(375,375,50)
