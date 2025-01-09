import math as m
import pygame as pg
import numpy as np

clock = pg.time.Clock()
wWidth = 300
wHeight = 300
window = pg.display.set_mode([wWidth, wHeight])


v = pg.math.Vector2(250,250)

color = (255,255,255)
contgame = True
while contgame == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            contgame = False
        if event.type == pg.MOUSEBUTTONDOWN:
            m_x, m_y = pg.mouse.get_pos()
            v[0] = m_x
            v[1] = m_y
            s = m_y/m_x
            print(s)
            # if rect.clipline(0,0,v[0],v[1]):
            #     color = (255,0,0)
            #     print("Colliding.")
            lin = np.linspace(0,v.length(),50)
            for i in lin:
                coords = i, i*s
                print(coords)
                print(m_x, m_y)
                if rect.collidepoint(coords[0],coords[1]):
                    color = (255,0,0)
                    print("Colliding.")
                    break
                else:
                    color = (255,255,255)
    window.fill((0,0,0))
    graph = pg.draw.line(window,color,(0,0),v,3)
    rect = pg.draw.rect(window,(200,200,255),(150,150,50,50))
    pg.display.flip()

    clock.tick(30)
pg.quit()