import pgzrun
import random
WIDTH=700
HEIGHT=600
GS=Actor("image-5")
GS.x=300
GS.y=235
msg="Click on Cat"
counter=0
def draw():
    screen.fill("White")
    GS.draw()
    screen.draw.text(msg,(350,100),color="Black")
    screen.draw.text(str(counter),(50,50),color="Black")
def update():
    pass
def on_mouse_down(pos):
    global msg,counter
    if GS.collidepoint(pos):
        GS.x=random.randint(50,WIDTH-50)
        GS.y=random.randint(50,HEIGHT-50)
        msg="Enjoy clicking!"
        counter+=1
    else:
        msg="Oops! Not the Cat!"
pgzrun.go()