def setup(): # runs once
    size(300, 200)
    print("width =", width, "\nheight =", height) #system variables

def draw(): # runs like in a Netlogo forever loop
    background(220) # make the background grey

    point(110,80) # Create a point with x value 110 and y value 80

    line(300, 20, 350, 100) # Create a line from point (300, 20) to (350, 100)

    rect(200, 50, 70, 10) # rectangle: rect( xcoor, ycoor, width, height)

    ellipse(50, 200, 100, 10) # ellipse(xcoor, ycoor, width, height)

    circle (100,300,25) # circle(xcoor, ycoor,radius)


    fill(0) # make the letters black so I can see them
    text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
