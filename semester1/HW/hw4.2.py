###########
# YinYang #
###########
def setup():
    size(400,400)

def draw():
    background(220)
    no_stroke() #no outline

    #white large circle
    fill(255)
    circle(200,200,200)

    #black semicircle on the left side
    fill(0)
    arc(200,200,200,200,radians(90),radians(270),OPEN)

    #half size black circle on the bottom
    circle(200,250,100) 
    #half size white circle on the top
    fill(255)
    circle(200,150,100) 
    #quarter size white circle on the bottom
    circle(200,250,25)
    #quater size black circle on the top
    fill(0)
    circle(200,150,25)
    #black outline
    no_fill()
    stroke(0)
    circle(200,200,200)