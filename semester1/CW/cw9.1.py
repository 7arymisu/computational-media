def setup():
    size(600,200)

def draw():
    x = 100 # initialize loop variable
    while x < width:
        
    # use the loop variable
        stroke_weight(2)

        fill(255, 0, 0)
        circle(x, 100 , 50)

        fill(0, 255, 0)
        circle(x, 100, 35)

        fill(0, 0, 255)
        circle(x, 100, 20)

        fill(255, 255, 0)
        circle(x, 100, 10)

        # update the loop variable
        x = x + 100 
