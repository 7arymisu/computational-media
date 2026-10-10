def setup():
    size(400,400)

def draw():
    background("#CCF5FF")
    no_stroke()
    
    fill("#FF0000")
    ellipse(width/2,height,width-40,height-40)
    fill("#000000")
    arc(width/2,height,width-40,width-40,radians(270), radians(360))
    
    rect(width-150,0,150,200)
    
    fill("#FFCC00") #yellow
    ellipse(width-75,100,150,150)
    
    fill("#FF0000")
    rect(width/3,100,200,200)

    fill("#339933") #green
    rect(0,0,width/3,width/3)
    
    fill("#FFCC00") #yellow
    triangle(0,0,width/3,width/3,0,width/3*2)
    
    rect(width/3+200,300,width-(width/3+200),100)
    
    fill("#FFCCAA") #lighter yellow
    arc(width-75,100,150,150,radians(90),radians(180))
    
    fill("#339933") #green
    triangle(0,195,200,195,200,300)
    
    fill("#000000")

