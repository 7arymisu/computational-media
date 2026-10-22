# ================================
# Using Random to randomize size:
# ================================

# circW = None
# def setup():
#     size(400,400)
#     global circW
#     circW = random(50, 150)
# def draw():
#     background(220)
#     ellipse(200, 200, circW, 100)

# =================================
# Using Random to randomize color: 
# =================================

# cor=color(random(255),random(255),random(255))
# # Note: RGB has a 4th argument: Alpha (transparency)
# def setup():
#     size(400,400)
# def draw():
#     background(220)
#     fill(cor)
#     ellipse(200, 200, 100, 100)

# ===============
# HSB Color Mode 
# ===============

# def setup():
#     size(400,400)

# def draw():
#     background(220)
#     fill(0)
#     # text(str(mouse_x) + ", " + str(mouse_y), 20, 20)

#     color_mode(HSB,360,100,100, 1.0)

#     d = 60
#     dp5 = d + 5

#     text_size(20)
#     text("Saturation",50,25)
#     text("Brightness",240,25)   

#     sat = 10
#     for x in range(d+1,width-dp5*4,dp5):
#         for y in range(d+1,height-dp5,dp5):
#             fill(360,sat,100)
#             circle(x,y,d)
#             sat += 10

#     bri = 10
#     for x in range(d+1+dp5*3,width-dp5,dp5):
#         for y in range(d+1,height-dp5,dp5):
#             fill(360,100,bri)
#             circle(x,y,d)
#             bri += 10

#     color_mode(RGB,255,255,255,255)

# =============================
# HSB mode for random() colors 
# =============================

# def draw():
#     background(220)
#     fill(0)
#     #text(str(mouse_x) + ", " + str(mouse_y), 20, 20)

#     color_mode(HSB,360,100,100)

#     d = 60
#     dp5 = d + 5

#     for x in range(d+1,width-dp5,dp5):
#         for y in range(d+1,height-dp5,dp5):
#             fill(random(360),100,100)
#             circle(x,y,d)

#     color_mode(RGB,255,255,255)