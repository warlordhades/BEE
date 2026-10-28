import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 411

score = 0
game_over = False

bee = Actor("uno")
bee.pos = 100,100

flower = Actor("dos")
flower.pos = 200,200

def draw():
    screen.blit("C:/pygame/bee flower game ect ect/images/tres.png",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score: "+str(score),color="red",topright=(550,0))

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
            bee.y=bee.y+2
pgzrun.go()