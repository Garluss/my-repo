import sys
import pygame as pg
from classes import *
clock = pg.time.Clock()

pg.init()


#Todo
'''
Move towards player if he sees him

'''

global_size_mod = 3



wWidth = 100*global_size_mod
wHeight = 100*global_size_mod
window = pg.display.set_mode([wWidth, wHeight])

font = pg.font.SysFont("Arial", 24)

tick = 0
FPS = 30

map1 = Scene(900,900,"scenes/bigmap.png",window,global_size_mod)
map1.load()

player = Player(2,2,wWidth/2,wHeight/2,"player",window, global_size_mod)
enemy1 = Entity(1,1,200,150,"groopie",window,global_size_mod)
text_x = Text("wsd", font, 60, 10, (255,255,255), window)
text_y = Text("sdsd", font, 60, 30, (255,255,255), window)

contgame = True
while contgame == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            contgame = False
    window.fill((255,255,255))

    player.current_s_x = 0
    player.current_s_y = 0
    pressed_keys = pg.key.get_pressed()
    if pressed_keys[pg.K_d]:
        player.current_s_x = (player.s_x)
    if pressed_keys[pg.K_a]:
        player.current_s_x = -(player.s_x)
    if pressed_keys[pg.K_s]:
        player.current_s_y = (player.s_y)
    if pressed_keys[pg.K_w]:
        player.current_s_y = -(player.s_y)

    if tick % 30 == 0:
        for instance in Entity.instances:
            if instance.check_visual(player,200) == True:
                instance.set_path(player.x, player.y)
            else:
                instance.change_speeds()
        tick = 0

    enemy1.move()
    Scene.current_scene.draw()
    player.draw()
    enemy1.draw()
    img = pg.image.load("scenes/vignette.png")
    img = pg.transform.scale(img,(100*global_size_mod,100*global_size_mod))
    rect = img.get_rect()
    rect.center = wWidth/2, wHeight/2
    window.blit(img, rect)
    if player.col_dec() == False:
        Scene.current_scene.move(player.current_s_x, player.current_s_y)
        [instance.shift(player.current_s_x,player.current_s_y) for instance in Entity.instances]
    player.world_x = -(Scene.current_scene.x-900)
    player.world_y = -(Scene.current_scene.y-900)
    text_x.set_text(str(f"X: {enemy1.world_x}, {player.world_x}"))
    text_y.set_text(str(f"Y: {enemy1.world_y}, {player.world_y}"))
    text_x.draw()
    text_y.draw()
    pg.display.flip()
    tick += 1
    clock.tick(FPS)

pg.quit()