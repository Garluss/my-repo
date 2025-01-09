import sys
import pygame as pg
from classes import *
clock = pg.time.Clock()

pg.init()


#Todo
'''
Check collission for all objects

Make world navigation system

Implement enemies

Tidy the class file / make more class files

Make it so that the collission map uses the actual window coordiantes, and not 1/3

Fix the collission check to use the actual speed, and not the constant values (1 and -1)
- Alternatively reset the coordinates rather than changing the speed

Implement hitboxes to tidy collission check and register enemy and player hits
- This can probably be done by scaling the image before taking the pixel array


Make more weapons
Loot
Different stats
Ammo and HUD
'''





wWidth = 600
wHeight = 300
window = pg.display.set_mode([wWidth, wHeight])

font = pg.font.SysFont("Arial", 24)

colmap = ColMap("col2",600,300,window)
startermap = Scene("scene2",600,300,colmap,window)
goober = Goober(0,0,wWidth/2,wHeight/2,"goober",window)
gub = Item("tommygub")
goober.equip(gub)

tick = 0
FPS = 60
backwards = False

contgame = True
while contgame == True:
    tick += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            contgame = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                klass = Projectile
                instance = klass(goober.x,goober.y,10,"bullet","goober",window,1)
                temp_x, temp_y = pg.mouse.get_pos()
                instance.set_path(temp_x, temp_y)
    window.fill((255,255,255))

    if tick % 10 == 0:
        for instt in Sprite.instances:
            instt.tick_animation()
        tick = 0

    goober.speed_x = 0
    goober.speed_y = 0
    pressed_keys = pg.key.get_pressed()
    if goober.is_sprite_busy() == False:
        if pressed_keys[pg.K_d]:
            goober.speed_x = 1
            goober.set_state("walk")
            backwards = False
        if pressed_keys[pg.K_a]:
            goober.speed_x = -1
            goober.set_state("walk")
            backwards = True
        if pressed_keys[pg.K_s]:
            goober.speed_y = 1
            goober.set_state("walk")
        if pressed_keys[pg.K_w]:
            goober.speed_y = -1
            goober.set_state("walk")
        if True not in pressed_keys:
            goober.set_state("idle")

    startermap.load()
    if goober.collission_dec() == False:
        goober.move()
    goober.draw(28*3,28*3,backwards)
    for instt in Projectile.p_instances:
        if instt.queue_destruction() != True:
            instt.move()
            instt.draw(28*3,28*3)
        else:
            Projectile.p_instances.remove(instt)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()