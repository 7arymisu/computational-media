def setup():
    size(220,340)

def draw():
    background(220)
    draw_robot()

def draw_robot():
    fill(255)
    rect(40,80,140,80) #head
    rect(100,160,20,20) #neck
    rect(60,180,100,60) #body

    line(80,240,80,280) #left leg
    arc(80,290,25,25,radians(180),radians(360),CHORD) #left foot
    line(140,240,140,280) #right leg
    arc(140,290,25,25,radians(180),radians(360),CHORD) #left foot

    arc(110,80,60,40,radians(180),radians(360)) #hat

    line(110,60,110,40) #antena line
    circle(110,30,20) #antenna top
    circle(80,120,40) #left eye
    circle(80,120,20) #left eyeball
    circle(140,120,40) #right eye
    circle(140,120,20) #right eyeball
    rect(80,200,60,10) #tummy
    circle(110,225,15) #belly button

